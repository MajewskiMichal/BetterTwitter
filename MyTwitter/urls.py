from django.conf.urls import url
from MyTwitter import views



urlpatterns = [
    url(r'^$', views.TweetViewAll.as_view()),

]