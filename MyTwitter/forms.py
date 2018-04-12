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


class UserForm(forms.Form):
    login = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, max_length=20)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None

    def clean(self):
        cleaned_data = super().clean()

        user = authenticate(
            username=cleaned_data['login'],
            password=cleaned_data['password']
        )

        if user is None:
            raise forms.ValidationError('Invalid credentials')

        self.user = user
        return cleaned_data


class

