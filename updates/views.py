from django.shortcuts import render
from django.views.generic import TemplateView
from novels.models import NovelModel
from datetime import datetime

# Create your views here.
class UpdatesView(TemplateView):
    template_name = r"updates\index.html"
    
    def get(self, request):
        all_novels = NovelModel.objects.all()
        # latest_novels = all_novels.order_by("last_edited")[(len(all_novels)-20):][::-1]
        latest_novels = []
        datetime_format = []

        for i in all_novels:
            datetime_format.append((datetime.strptime(i.last_edited, r"%Y-%m-%d %H:%M:%S"), i))    
        # import pdb; pdb.set_trace()
        datetime_format = sorted(datetime_format, key=lambda x: x[0], reverse=True)

        for z in datetime_format:
            latest_novels.append(z[1])
            
        latest_novels = latest_novels[0:21]
        
        ctx = {
            "latest_novels": latest_novels,
        }
        return render(request, self.template_name, context=ctx)

