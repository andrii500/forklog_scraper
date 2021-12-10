from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<slug:pk>', views.NewsView.as_view(), name='news_page'),

    # path('api/v1/base-auth/', include('rest_framework.urls')),
    # path('api/v1/pages/', include('scraper.api.urls')),
    # path('api/v1/auth/', include('djoser.urls')),
    # path('api/v1/auth_token/', include('djoser.urls.authtoken')),

    path('api/v1/', include('scraper.api.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
