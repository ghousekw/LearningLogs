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

