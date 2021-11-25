from django.db import models


class Page(models.Model):
    topic_link = models.TextField()
    img_link = models.TextField()
    title = models.TextField()
    article_date = models.DateField()
    article_author = models.TextField()
    tags = models.TextField()
    text = models.TextField()

    class Meta:
        ordering = ['-article_date']

    def __str__(self):
        return f"{self.title}"
