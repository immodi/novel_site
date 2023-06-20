from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel

# Create your views here.
class HomeView(TemplateView):
    template_name = "home\index.html"
    
    def get(self, request):
        all_novels = NovelModel.objects.all()
        hot_novels = all_novels.order_by("views")[(len(all_novels)-20):][::-1]
        
        # import pdb; pdb.set_trace()
        ctx = {
            "hot_novels": hot_novels,
        }
        return render(request, self.template_name, context=ctx)

