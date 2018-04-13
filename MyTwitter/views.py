from django.shortcuts import render
from django.views import View
from .models import Tweet, Comment
from .forms import TweetForm, UserForm, SignUpForm, CommentForm
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()


class TweetViewAll(LoginRequiredMixin, ListView):
    model = Tweet
    context_object_name = 'tweets'
    login_url = 'mytwitter/login'


class CreateTweetView(CreateView):
    form_class = TweetForm
    template_name = 'MyTwitter/Tweet_form.html'
    success_url = '/mytwitter'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class LoginView(View):
    form_class = UserForm
    template_name = 'MyTwitter/user_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            login(request, form.user)
            return redirect('/mytwitter')
        else:
            return render(request, self.template_name, {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/mytwitter/login')


class CreateUserView(CreateView):
    form_class = SignUpForm
    success_url = '/mytwitter'
    template_name = 'MyTwitter/create_user_form.html'

    def form_valid(self, form):

        valid = super(CreateUserView, self).form_valid(form)
        username, password = \
            form.cleaned_data.get('username'), \
            form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class UserTweetsView(View):
    template_name = 'MyTwitter/user_tweet_list.html'

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id )
        return render(request, self.template_name, {'user': user})



class CommentsView(View):
    form_class = CommentForm
    template_name = 'MyTwitter/comment_form.html'

    def get(self, request, tweet_id):
        comments = Comment.objects.filter(tweet=tweet_id)
        tweet = get_object_or_404(Tweet, id=tweet_id)
        return render(request,
                      self.template_name,
                      {
                       'form': self.form_class(),
                       'comments': comments,
                       'tweet': tweet
                        })


