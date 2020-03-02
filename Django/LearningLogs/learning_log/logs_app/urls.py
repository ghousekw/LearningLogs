from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('topics/', views.topics, name="topics"),  # show all entries
    path('topics/<str:topic_id>', views.topic, name="topic"),  # show individual entries
]
