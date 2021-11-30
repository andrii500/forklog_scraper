from rest_framework import serializers
from scraper.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'article_date', 'article_author', 'tags']
