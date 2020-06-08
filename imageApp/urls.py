
from django.urls import path,re_path
from imageApp.views import gelaryApp, mediaApp

urlpatterns = [
    path('',gelaryApp),
    re_path('media/', mediaApp)
]