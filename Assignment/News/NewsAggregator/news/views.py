# import requests
# from django.shortcuts import render, redirect
# from bs4 import BeautifulSoup as BSoup
# from .models import Headline

# requests.packages.urllib3.disable_warnings()

# # Create your views here.
# def scrape(request):
#     session = requests.Session()
#     session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
#     url = "https://www.theonion.com/"
#     content = session.get(url, verify=False).content
#     soup = BSoup(content, "html.parser")
#     News = soup.find_all('div', {"class":"curation-module__item"})
#     for artcile in News:
#         main = artcile.find_all('a')[0]
#         link = main['href']
#         image_src = str(main.find('img')['srcset']).split(" ")[-4]
#         title = main['title']
#         new_headline = Headline()
#         new_headline.title = title
#         new_headline.url = link
#         new_headline.image = image_src
#         new_headline.save()
#     return redirect("../")

# # def news_list(request):
# #     headlines = Headline.objects.all()[::-1]
# #     context = {
# #         'object_list': headlines,
# #     }
# #     return render(request, "news/home.html", context)
# def news_list(request):
#     headlines = Headline.objects.all()[::-1]
#     context = {
#         'object_list': headlines,
#     }
#     return render(request, "news/home.html", context)
from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect

import feedparser
import datetime

# Create your views here.

def articles_list(request):
    articles = Article.objects.all()

    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]

    return render(request, 'news/articles_list.html', {'rows': rows})

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'news/feeds_list.html', {'feeds': feeds})

def new_feed(request):
    if request.method == "POST":
        form = FeedForm(request.POST)
        if form.is_valid():
            feed = form.save(commit=False)

            existingFeed = Feed.objects.filter(url = feed.url)
            if len(existingFeed) == 0:
                feedData = feedparser.parse(feed.url)

                # set some fields
                feed.title = feedData.feed.title
                feed.save()

                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description

                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    dateString = d.strftime('%Y-%m-%d %H:%M:%S')

                    article.publication_date = dateString
                    article.feed = feed
                    article.save()

            return redirect('news.views.feeds_list')
    else:
        form = FeedForm()
    return render(request, 'news/new_feed.html', {'form': form})