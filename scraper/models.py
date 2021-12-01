from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Page(models.Model):
    topic_link = models.TextField(verbose_name='Topic link')
    img_link = models.TextField(verbose_name='Image link')
    title = models.TextField(verbose_name='Title of the topic')
    article_date = models.DateField(verbose_name='Date of article publication')
    article_author = models.TextField(verbose_name='Article author')
    tags = models.TextField(verbose_name='Tags')
    text = models.TextField(verbose_name='Article')
    user = models.ForeignKey(User, verbose_name='User login', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-article_date']

    def __str__(self):
        return f"{self.title}"
