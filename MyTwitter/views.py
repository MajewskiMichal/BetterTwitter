from django.shortcuts import render
from django.views import View
from .models import Tweet


class TweetViewAll(View):

    def get(self, request):

        return render(request, "MyTwitter/AllTweets.html", {'tweets': Tweet.objects.all()})



