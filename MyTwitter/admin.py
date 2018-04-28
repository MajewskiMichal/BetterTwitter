from django.contrib import admin
from django import forms
from .models import Tweet, Message, Comment
from django.utils.html import format_html


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'creation_date', 'user', 'num_of_likes', 'comments']
    # we don't want anybody to manipulate with our tweets, their authors or users who likes them,
    #  so no links to changes:
    list_display_links = None

    def num_of_likes(self, obj):
        return obj.likes.count()
    num_of_likes.short_description = 'likes'

    def comments(self, obj):
        html = "<select>"
        comments = obj.comment_set.all()
        if list(comments) == []:
            return 'no comments'
        for comment in comments:
            html += '<option>{}</option>'.format(comment)
        html += '</select>'
        return format_html(html)

        # return ','.join(obj.comment_set.all().values_list('comment', flat=True))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'creation_date', 'user', 'tweet', 'tweet_user']

    # we don't want anybody to manipulate with comments, and their authors,
    #  so no links to changes:
    list_display_links = None

    def tweet_user(self, obj):
        return obj.tweet.user
    tweet_user.short_description = 'who tweeted'


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'who_sent', 'to', 'date_sent', 'time_read']

    exclude = ['is_read', 'time_read']

    # we don't want anybody to manipulate with messages, or conversations participants,
    #  so no links to changes:
    list_display_links = None




















