from django.conf.urls import url
from MyTwitter import views


urlpatterns = [
    url(r'^$', views.TweetViewAll.as_view(), name='all-tweets'),
    url(r'^create-tweet/$', views.CreateTweetView.as_view(), name='create-tweet'),
    url(r'login/$', views.LoginView.as_view(), name='login'),
    url(r'logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'add-user/$', views.CreateUserView.as_view(), name='create-user'),
    url(r'user-tweets/(?P<user_id>(\d)+)/$', views.UserTweetsView.as_view(), name='user-tweets'),
    url(r'comments/(?P<tweet_id>(\d)+)/$', views.CommentsView.as_view(), name='comments')
]