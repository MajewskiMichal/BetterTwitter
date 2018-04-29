from rest_framework import serializers
from MyTwitter.models import Tweet


class TweetSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Tweet
        fields = [
           'pk',
           'user',
           'content',
           'creation_date',
           'likes',
            ]

        read_only_fields = ['user']

    # concerts to JSON
    # validatons for data passed