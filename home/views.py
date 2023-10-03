from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel
from random import randrange

class HomeView(TemplateView):
    template_name = "home\index.html"
    
    def get(self, request):
        random_start = randrange(31)
        hot_novels = NovelModel.objects.all()[random_start:random_start+21]
        # hot_novels = all_novels.order_by("id")[(len(all_novels)-21):][::-1]
        
        # import pdb; pdb.set_trace()
        ctx = {
            "hot_novels": hot_novels,
        }
        return render(request, self.template_name, context=ctx)


class PrivacyView(TemplateView):
    template_name = "home\privacy.html"
    
    def get(self, request):
        return render(request, self.template_name)


class DmcaView(TemplateView):
    template_name = "home\dmca.html"
    
    def get(self, request):
        return render(request, self.template_name)


class TosView(TemplateView):
    template_name = "home\\tos.html"
    
    def get(self, request):
        return render(request, self.template_name)

