from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, Textarea, PasswordInput
from django.contrib.auth import authenticate, get_user_model
from .models import Tweet
from django.core.exceptions import ValidationError
User = get_user_model()


class TweetForm(ModelForm):

    class Meta:
        model = Tweet
        fields = ['content']

        widgets = {
                'content': Textarea(attrs={'cols': 30, 'rows': 5}),
        }


class UserForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

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


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



