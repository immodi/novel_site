from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel


class NovelsView(TemplateView):
    template_name = r"novels\index.html"

    def get(self, request, current_page_number=1):

        def novels_data_extractor(data={}):
            import json
            for i in novels:
                data[i.name] = i.chapters
            with open("current_chapters.json", "w") as file:
                file.write(json.dumps(data, indent=4))
            return
            
        current_page_number -= 1
        novels = list(NovelModel.objects.all().order_by("id"))

        # novels_data_extractor()  # Extract database data locally

        novels_formated = []
        if (len(novels) / 20).is_integer():
            pages_number = int(len(novels) / 21)
        else:
            pages_number = int(len(novels) / 21) + 1

        pages_array = []

        for i in range(pages_number):
            novels_formated.append(novels[0:21])
            novels = novels[20:]
            pages_array.append(i+1)
        
        
        # import pdb; pdb.set_trace()
        return render(request, self.template_name, context={"novels": novels_formated[current_page_number], "total_pages": pages_array,})
        

class NovelInfoView(TemplateView):
    template_name = r"novels\description.html"

    def get(self, request, current_page_number=0):
        novel_name = request.GET.get("novel_name").split('/')[0]
        try:
            current_page_number = int(request.GET.get("novel_name").split('/')[1]) - 1
            if current_page_number < 0:
                current_page_number = 0
                pages_array = (1, 2)
        except Exception:
            current_page_number = 0

        novel = NovelModel.objects.get(name=novel_name)
        
        novel_chapters = novel.chapters
        # chapter_names = list(novel.data)[current_page_number*40:][0:40]
        chapter_names = [(chapter, list(novel.data).index(chapter)+1) for chapter in list(novel.data)[current_page_number*40:]][0:40]

        novel.views += 1
        author = novel.info["author"]
        state = novel.info["state"]
        tags = novel.info["tags"]
        summary = novel.info["summary"]
        
        novel.save()
        # import pdb; pdb.set_trace()
        
        if current_page_number + 1 == int((novel_chapters / 40) + 2) - 1:
            pages_array = (current_page_number, current_page_number + 1)
        elif current_page_number == 0:
            pages_array = (1, 2)
        else:
            pages_array = (current_page_number, current_page_number+1, current_page_number + 2)

        ctx = {
            "name": novel_name,
            "chapters": novel_chapters,
            "chapter_names": chapter_names,
            "cover": novel.cover_url,
            "views": novel.views,
            "author": author,
            "state": state,
            "tags": tags,
            "summary": summary,
            "first_chapter": f"/novel/novel_name={novel_name}/chapter=1",
            "last_chapter": f"/novel/novel_name={novel_name}/chapter={novel_chapters}", 
            "total_pages": pages_array

        }

        return render(request, self.template_name, context=ctx)


class NovelReaderView(TemplateView):
    template_name = r"novels\reader.html"

    def get(self, request, name, chapter):
        def url_generator(novel_name:str, current_chapter: int, max_chapters: int, mode: int, url=""):
            if mode == 1:
                if current_chapter == max_chapters:
                    url = "#"
                else:
                    url = f"/novel/novel_name={novel_name}/chapter={current_chapter + 1}"
            elif mode == -1:
                if current_chapter == 1:
                    url = "#"
                else:
                    url = f"/novel/novel_name={novel_name}/chapter={current_chapter - 1}"
            return url

        novel = NovelModel.objects.get(name=name)
        max_chapters = novel.chapters
        novel_name = novel.name
        data = novel.data
        titles_orderd = list(data.keys())
        content = data[titles_orderd[chapter-1]]
        next_url = url_generator(novel_name, chapter, max_chapters, mode=1)
        previous_url = url_generator(novel_name, chapter, max_chapters, mode=-1)
        home_url = f"/novel?novel_name={novel_name}"
        # import pdb; pdb.set_trace()

        return render(request, self.template_name, context={"name": name, "content": content, "next_url": next_url, "previous_url": previous_url, "home_url": home_url, "chapter": chapter, })
