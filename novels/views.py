from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel
from novelsite import settings
import re

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

    def get(self, request):
        novel_name = request.GET.get("novel_name")
        novel = NovelModel.objects.get(name=novel_name)
        
        novel_chapters = novel.chapters
        chapter_names = novel.data
        novel.views += 1
        author = novel.info["author"]
        state = novel.info["state"]
        # rating = novel.info["rating"]
        # categories = novel.info["categories"]
        tags = novel.info["tags"]
        summary = novel.info["summary"]

        novel.save()


        ctx = {
            "name": novel_name,
            "chapters": novel_chapters,
            "chapter_names": chapter_names,
            "cover": novel.cover_url,
            "views": novel.views,
            "author": author,
            "state": state,
            # "rating": rating,
            # "categories": categories,
            "tags": tags,
            "summary": summary,
            "first_chapter": f"/novel/novel_name={novel_name}/chapter=1",
            "last_chapter": f"/novel/novel_name={novel_name}/chapter={novel_chapters}"
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
        titles_orderd = sorted(list(data.keys()), key=lambda s: int(re.search(r'\d+', s).group()))
        content = data[titles_orderd[chapter-1]]
        next_url = url_generator(novel_name, chapter, max_chapters, mode=1)
        previous_url = url_generator(novel_name, chapter, max_chapters, mode=-1)
        home_url = f"/novel?novel_name={novel_name}"
        # import pdb; pdb.set_trace()

        return render(request, self.template_name, context={"name": name, "content": content, "next_url": next_url, "previous_url": previous_url, "home_url": home_url, "chapter": chapter, })
