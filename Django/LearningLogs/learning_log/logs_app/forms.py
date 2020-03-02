from django import forms
from .models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # building a form from topic model and include only text field
        fields = ['text']
        # generate a label for a text field
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}