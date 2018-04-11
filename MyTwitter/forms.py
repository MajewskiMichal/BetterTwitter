from django import forms
from django.forms import ModelForm, Textarea
from django.contrib.auth import authenticate
from .models import Tweet


class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['content']

        widgets = {
        'content': Textarea(attrs={'cols': 60, 'rows': 10}),
    }