from django.contrib.auth.models import User
from rest_framework import serializers
from scraper.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['title', 'article_date', 'article_author', 'tags', 'user']

    user = serializers.ReadOnlyField(source='user.username')


class UserSerializer(serializers.ModelSerializer):
    pages = serializers.PrimaryKeyRelatedField(many=True, queryset=Page.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'pages']


# class PageDetailSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Page
#         fields = '__all__'
#
#
# class PageListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Page
#         fields = ('id', 'title', 'user')




