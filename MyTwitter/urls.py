from django.conf.urls import url
from MyTwitter import views


urlpatterns = [
    url(r'^$', views.TweetViewAll.as_view(), name='all-tweets'),
    url(r'^likes/(?P<tweet_id>(\d)+)/$', views.TweetLikeToggle.as_view(), name='likes'),
    url(r'^api/likes/(?P<tweet_id>(\d)+)/$', views.TweetLikeAPIToggle.as_view(), name='likes-api'),
    url(r'^create-tweet/$', views.CreateTweetView.as_view(), name='create-tweet'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^add-user/$', views.CreateUserView.as_view(), name='create-user'),
    url(r'^user-tweets/(?P<user_id>(\d)+)/$', views.UserTweetsView.as_view(), name='user-tweets'),
    url(r'^comments/(?P<tweet_id>(\d)+)/$', views.CommentsView.as_view(), name='comments'),
    url(r'^correspondence/(?P<user_id>(\d)+)/$', views.CorrespondenceView.as_view(), name='correspondence'),
    url(r'^user-site/$', views.UserSiteView.as_view(), name='user-site'),
    url(r'^update-user/$', views.UserUpdateView.as_view(), name='update-user'),
    url(r'^message/(?P<msg_id>(\d)+)/$', views.MessageView.as_view(), name='message')

]