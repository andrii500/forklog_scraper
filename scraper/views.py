from django.views.generic import TemplateView, ListView, DetailView
from rest_framework import viewsets, permissions
from .models import Page
from .serializers import PageSerializer
from .tasks import parse_pages


class IndexView(TemplateView):
    parse_pages.delay()
    template_name = 'base/index.html'


class NewsListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        queryset = Page.objects.all()
        return queryset


class NewsView(DetailView):
    model = Page
    template_name = 'scraper/page.html'


# Django Rest Framework
class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [permissions.IsAuthenticated]
