from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Tweet(models.Model):

    content = models.CharField(max_length=140)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')

    class Meta:
        ordering = ['-creation_date']

    def get_absolute_url(self):
        return reverse('user-tweets', kwargs={'user_id': self.user.id})

    def get_like_url(self):
        return reverse('likes', kwargs={'tweet_id': self.id})

    def get_like_api_url(self):
        return reverse('likes-api', kwargs={'tweet_id': self.id})

    def __str__(self):
        return self.content


class Comment(models.Model):

    comment = models.CharField(max_length=60)
    creation_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment


class Message(models.Model):

    subject = models.CharField(max_length=150)
    content = models.TextField()
    to = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    who_sent = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    time_read = models.DateTimeField(null=True)

    def __str__(self):
        return self.subject


