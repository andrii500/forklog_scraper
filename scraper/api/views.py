# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from scraper.models import Page
# from .serializers import PageSerializer


# class PageListApiView(APIView):
#
#     def get(self, request, *args, **kwargs):
#         pages = Page.objects.all()
#         serializer = PageSerializer(pages, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         data = {
#             'topic_link': request.data.get('topic_link'),
#             'img_link': request.data.get('img_link'),
#             'title': request.data.get('title'),
#             'article_date': request.data.get('article_date'),
#             'article_author': request.data.get('article_author'),
#             'tags': request.data.get('tags'),
#             'text': request.data.get('text'),
#         }
#         serializer = PageSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class PageDetailApiView(APIView):
#     def get_object(self, page_id):
#         try:
#             return Page.objects.get(id=page_id)
#         except Page.DoesNotExist:
#             return None
#
#     def get(self, request, page_id, *args, **kwargs):
#         page_instance = self.get_object(page_id)
#         if not page_instance:
#             return Response(
#                 {'res': 'Object with page id does not exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#
#         serializer = PageSerializer(page_instance)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, page_id, *args, **kwargs):
#         page_instance = self.get_object(page_id)
#         if not page_instance:
#             return Response(
#                 {'res': 'Object with page id does not exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         data = {
#             'topic_link': request.data.get('topic_link'),
#             'img_link': request.data.get('img_link'),
#             'title': request.data.get('title'),
#             'article_date': request.data.get('article_date'),
#             'article_author': request.data.get('article_author'),
#             'tags': request.data.get('tags'),
#             'text': request.data.get('text'),
#         }
#         serializer = PageSerializer(instance=page_instance, data=data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, page_id, *args, **kwargs):
#         page_instance = self.get_object(page_id)
#         if not page_instance:
#             return Response(
#                 {'res': 'Object with page id does not exists'},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#         page_instance.delete()
#         return Response(
#             {'res': 'Object deleted!'},
#             status=status.HTTP_200_OK
#         )

# from rest_framework import generics
# from .serializers import PageDetailSerializer, PageListSerializer
# from scraper.models import Page
# from .permissions import IsOwnerOrReadOnly
# from rest_framework.permissions import IsAuthenticated
#
#
# class PageCreateView(generics.CreateAPIView):
#     serializer_class = PageDetailSerializer
#
#
# class PagesListView(generics.ListAPIView):
#     serializer_class = PageListSerializer
#     queryset = Page.objects.all()
#     permission_classes = (IsAuthenticated, )
#
#
# class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = PageDetailSerializer
#     queryset = Page.objects.all()
#     permission_classes = (IsOwnerOrReadOnly, )


from django.contrib.auth.models import User
from scraper.models import Page
from .serializers import PageSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class PageList(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'pages': reverse('page-list', request=request, format=format)
    })
