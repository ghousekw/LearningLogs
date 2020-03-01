# from django.urls import path
# from .views import scrape, news_list

# urlpatterns = [
#     path('scrape/', scrape, name="scrape"),
#     path('', news_list, name="home"),
# ]

# from django.urls import path
# from news.views import scrape, news_list
# urlpatterns = [
#   path('scrape/', scrape, name="scrape"),
#   path('', news_list, name="home"),
# ]
from django.urls import path
from . import views


urlpatterns = [
    path('', views.articles_list, name='articles_list'),
    path('feeds/new', views.new_feed, name='feed_new'),
    path('feeds/', views.feeds_list, name='feeds_list')

]