from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    """Home page for learning log"""
    return render(request, 'logs_app/index.html')


def topics(request):
    """Show all topics from the database"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'logs_app/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'logs_app/topic.html', context)