from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PageList,
    PageDetail,
    UserList,
    UserDetail,
    api_root
    # PageCreateView,
    # PagesListView,
    # PageDetailView
)


urlpatterns = [
    # path('', PageListApiView.as_view()),
    # path('<int:page_id>/', PageDetailApiView.as_view()),
    # path('page/create/', PageCreateView.as_view()),
    # path('all/', PagesListView.as_view()),
    # path('page/detail/<int:pk>/', PageDetailView.as_view()),
    path('', api_root),
    path('pages/', PageList.as_view(), name='page-list'),
    path('pages/<int:pk>/', PageDetail.as_view(), name='page-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
