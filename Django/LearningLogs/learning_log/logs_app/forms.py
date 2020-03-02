from django import forms
from .models import *


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        # building a form from topic model and include only text field
        fields = ['text']
        # generate a label for a text field
        labels = {'text': ''}
