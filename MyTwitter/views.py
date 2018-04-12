from django.shortcuts import render
from django.views import View
from .models import Tweet
from .forms import TweetForm, UserForm
from django.views.generic import CreateView, ListView
from django.contrib.auth import get_user_model, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


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

