# Generated by Django 3.2.9 on 2021-11-25 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0005_alter_page_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['-article_date']},
        ),
    ]
