from django.urls import path
from novels.views import NovelsView, NovelInfoView, NovelReaderView

urlpatterns = [
    path('novels', NovelsView.as_view(), name="novels"),
    path('novels/<int:current_page_number>', NovelsView.as_view(), name="novels"),
    path('novel/', NovelInfoView.as_view(), name="novel"),
    path('novel/<int:current_page_number>', NovelInfoView.as_view(), name="novel"),
    path('novel/novel_name=<str:name>/chapter=<int:chapter>', NovelReaderView.as_view(), name="chapter")
]
