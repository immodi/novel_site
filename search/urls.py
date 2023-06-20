from django.urls import path
from search.views import SearchView, NovelValidationView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('search', SearchView.as_view(), name="search"),
    path('search-novel', csrf_exempt(NovelValidationView.as_view()), name="search_novel"),
]
