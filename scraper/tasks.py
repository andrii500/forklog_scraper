import requests
import datetime as datetime
from celery import shared_task
from bs4 import BeautifulSoup
from .models import Page


@shared_task
def parse_pages():
    url = 'https://forklog.com/news/page/'
    page_num = 1

    while True:
        if requests.get(f"{url}{page_num}"):
            r = requests.get(f"{url}{page_num}")
            soup = BeautifulSoup(r.text, features="html.parser")
            divs = soup.find_all('div', {'class': 'post_item'})

            for div in divs:
                link = div.find('a').get('href')
                parse_page(link)
            page_num += 1
        else:
            break


def parse_page(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.text, features='html.parser')

    if soup.find('div', {'class': 'post_content'}):
        title = soup.find('h1').get_text()

        article_date_ = soup.find('span', {'class': 'article_date'}).get_text()
        article_date = datetime.datetime.strptime(article_date_, '%d.%m.%Y').date()

        article_author = soup.find('a', {'class': 'article_author'}).get_text()

        try:
            img_link = soup.find('div', {'class': 'article_image'}).find('img').get('src')
        except:
            img_link = 'https://forklog.com/wp-content/uploads/blockchain-2.jpg'

        if soup.find('div', {'class': 'post_tags_top'}):
            post_tags = soup.find('div', {'class': 'post_tags_top'}).find_all('a')
            tags = ''
            for tag in post_tags:
                tags += tag.get_text()
        else:
            tags = ''

        text = soup.find('div', {'class': 'post_content'}).get_text()
        text = text.replace(title, '')
        text = text.replace(article_date_, '')
        text = text.replace(article_author, '')
        text = text.replace(tags, '')
        text = text.replace('Нашли ошибку в тексте? Выделите ее и нажмите CTRL+ENTER', '')
        text = text.strip('\n')

        if not Page.objects.filter(topic_link=link).exists():
            Page.objects.create(topic_link=link, img_link=img_link, title=title, article_author=article_author,
                                article_date=article_date, tags=tags, text=text)
