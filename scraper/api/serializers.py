from rest_framework import serializers
from scraper.models import Page


# class PageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Page
#         fields = ['title', 'article_date', 'article_author', 'tags']


class PageDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Page
        fields = '__all__'


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('id', 'title', 'user')
