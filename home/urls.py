from django.urls import path
from home.views import HomeView, PrivacyView, DmcaView, TosView

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('dmca', DmcaView.as_view(), name="dmca"),
    path('privacy', PrivacyView.as_view(), name="privacy"),
    path('tos', TosView.as_view(), name="tos"),
]
