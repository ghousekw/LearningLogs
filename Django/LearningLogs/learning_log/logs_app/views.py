from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse, redirect
from .models import *
from .forms import TopicForm, EntryForm


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


def new_topic(request):
    """Add a new Form"""
    if request.method != 'POST':
        #  When blank form is submitted
        form = TopicForm()
    else:
        #  when post method is submitted, process data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))

    context = {'form': form}
    return render(request, 'logs_app/new_topic.html', context)


def new_entry(request, topic_id):
    """Add a new entry for a particular topic"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'logs_app/new_entry.html', context)
