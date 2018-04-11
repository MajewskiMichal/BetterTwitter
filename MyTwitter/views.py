from django.shortcuts import render
from django.views import View
from .models import Tweet
from .forms import TweetForm
from django.views.generic import CreateView


class TweetViewAll(View):

    def get(self, request):

        return render(request, "MyTwitter/AllTweets.html", {'tweets': Tweet.objects.all()})


class CreateTweetView(CreateView):
    form_class = TweetForm
    template_name = 'MyTwitter/Tweet_form.html'
    success_url = '/mytwitter'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
