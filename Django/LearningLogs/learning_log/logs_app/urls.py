from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('topics/', views.topics, name="topics"),  # show all entries
    path('topics/<str:topic_id>', views.topic, name="topic"),  # show individual entries
    path('new_topic/', views.new_topic, name="new_topic"),  # create a new topic
    path('new_entry/<str:topic_id>', views.new_entry, name="new_entry"),
]
