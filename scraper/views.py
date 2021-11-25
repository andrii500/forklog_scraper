from django.views.generic import TemplateView, ListView, DetailView
from .models import Page


class IndexView(TemplateView):
    template_name = 'base/index.html'


class NewsListView(ListView):
    paginate_by = 10

    def get_queryset(self):
        queryset = Page.objects.all()
        return queryset


class NewsView(DetailView):
    model = Page
    template_name = 'scraper/page.html'
