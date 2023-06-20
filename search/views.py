from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel
from django.http import JsonResponse
import json


class SearchView(TemplateView):
    template_name = r"search\index.html"

    def get(self, request):
        return render(request, self.template_name)


class NovelValidationView(TemplateView):
    def post(self, request):
        data = json.loads(request.body)
        novel_name = data["name"]

        if NovelModel.objects.filter(name__contains=str(novel_name)).exists():
            novels_matched = NovelModel.objects.filter(
                name__contains=str(novel_name))
            novels_data = []
            for i in novels_matched:
                novel_name = i.name
                novel_cover = i.cover_url
                novel_chapters = i.chapters
                novels_data.append((novel_name, novel_cover, novel_chapters))
            # import pdb; pdb.set_trace()
            return JsonResponse({"novels": novels_data})
        return JsonResponse({"novels": []})
