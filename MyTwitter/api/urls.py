from django.conf.urls import url


from . import views
urlpatterns = [
    url(r'^(?P<pk>(\d)+)/$', views.TweetRudView.as_view(), name='tweet-rud'),
    url(r'^create/$', views.TweetCreateView.as_view(), name='tweet-create'),

]