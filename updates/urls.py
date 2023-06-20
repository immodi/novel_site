from django.urls import path
from updates.views import UpdatesView

urlpatterns = [
    path('updates', UpdatesView.as_view(), name="updates"),
]
