from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<slug:pk>', views.NewsView.as_view(), name='news_page'),
]
