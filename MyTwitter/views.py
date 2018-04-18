from django.db.models import Q
from django.views import View
from .models import Tweet, Comment, Message
from .forms import (TweetForm,
                    UserForm,
                    SignUpForm,
                    CommentForm,
                    MessageForm,
                    CorrespondenceForm
                    )
from django.views.generic import (CreateView,
                                  ListView,
                                  UpdateView,
                                  DetailView
                                  )
from django.contrib.auth import (get_user_model,
                                 login,
                                 logout,
                                 authenticate
                                 )
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
User = get_user_model()


class TweetViewAll(LoginRequiredMixin, ListView):
    model = Tweet
    context_object_name = 'tweets'
    login_url = 'mytwitter/login'


class CreateTweetView(CreateView):
    form_class = TweetForm
    template_name = 'MyTwitter/tweet_form.html'
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

    def post(self, request, tweet_id):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = self.request.user
            tweet = get_object_or_404(Tweet, id=tweet_id)
            comment = form.cleaned_data['comment']
            Comment.objects.create(comment=comment, user=user, tweet=tweet)
            return redirect('comments', tweet_id=tweet_id)
        return redirect('comments', tweet_id=tweet_id)


class UserSiteView(View):
    form_class = CorrespondenceForm
    template_name = 'MyTwitter/user_site.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class(self.request.user)})

    def post(self, request):
        form = self.form_class(self.request.user, data=request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            return redirect('correspondence', user_id=user.id)
        return render(request, self.template_name, {'form': form})


class UserUpdateView(UpdateView):
    form_class = SignUpForm
    template_name = 'MyTwitter/update_user_form.html'
    success_url = '/mytwitter/login'

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj


class CorrespondenceView(View):
    form_class = MessageForm
    template_name = 'MyTwitter/message_form.html'

    def get(self, request, user_id):
        sender = self.request.user
        receiver = User.objects.get(id=user_id)
        messages = Message.objects.filter(Q(who_sent=sender, to=receiver) | Q(who_sent=receiver, to=sender))
        return render(request, self.template_name, {'form': self.form_class(),
                                                    'receiver': receiver,
                                                    'messages': messages,
                                                    })

    def post(self, request, user_id):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            sender = self.request.user
            receiver = User.objects.get(id=user_id)
            Message.objects.create(subject=form.cleaned_data['subject'],
                                   content=form.cleaned_data['content'],
                                   who_sent=sender,
                                   to=receiver)
            return redirect('correspondence', user_id=receiver.id)
        return render(request, self.template_name, {'form': form})


class MessageView(DetailView):
    model = Message
    pk_url_kwarg = 'msg_id'




























