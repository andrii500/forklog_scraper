from django.conf.urls import url
from django.urls import path, include
from .views import (
    PageListApiView,
    PageDetailApiView
)


urlpatterns = [
    path('', PageListApiView.as_view()),
    path('<int:page_id>/', PageDetailApiView.as_view()),
]
