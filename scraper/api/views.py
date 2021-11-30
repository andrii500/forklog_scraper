from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scraper.models import Page
from .serializers import PageSerializer


class PageListApiView(APIView):

    def get(self, request, *args, **kwargs):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = {
            'topic_link': request.data.get('topic_link'),
            'img_link': request.data.get('img_link'),
            'title': request.data.get('title'),
            'article_date': request.data.get('article_date'),
            'article_author': request.data.get('article_author'),
            'tags': request.data.get('tags'),
            'text': request.data.get('text'),
        }
        serializer = PageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PageDetailApiView(APIView):
    def get_object(self, page_id):
        try:
            return Page.objects.get(id=page_id)
        except Page.DoesNotExist:
            return None

    def get(self, request, page_id, *args, **kwargs):
        page_instance = self.get_object(page_id)
        if not page_instance:
            return Response(
                {'res': 'Object with page id does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PageSerializer(page_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, page_id, *args, **kwargs):
        page_instance = self.get_object(page_id)
        if not page_instance:
            return Response(
                {'res': 'Object with page id does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'topic_link': request.data.get('topic_link'),
            'img_link': request.data.get('img_link'),
            'title': request.data.get('title'),
            'article_date': request.data.get('article_date'),
            'article_author': request.data.get('article_author'),
            'tags': request.data.get('tags'),
            'text': request.data.get('text'),
        }
        serializer = PageSerializer(instance=page_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, page_id, *args, **kwargs):
        page_instance = self.get_object(page_id)
        if not page_instance:
            return Response(
                {'res': 'Object with page id does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        page_instance.delete()
        return Response(
            {'res': 'Object deleted!'},
            status=status.HTTP_200_OK
        )