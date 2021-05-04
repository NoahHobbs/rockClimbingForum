from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=200)
    date = models.DateTimeField('created date')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)


class Comment(models.Model):
    username = models.CharField(max_length=200)
    date = models.DateTimeField('created date')
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=200)
    post = models.ForeignKey(Post, related_name="comments",
                             on_delete=models.CASCADE)
