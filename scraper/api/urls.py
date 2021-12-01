from django.urls import path, include
from .views import (
    # PageListApiView,
    # PageDetailApiView
    PageCreateView,
    PagesListView,
    PageDetailView
)

app_name = 'page'


urlpatterns = [
    # path('', PageListApiView.as_view()),
    # path('<int:page_id>/', PageDetailApiView.as_view()),
    path('page/create/', PageCreateView.as_view()),
    path('all/', PagesListView.as_view()),
    path('page/detail/<int:pk>/', PageDetailView.as_view()),
]
