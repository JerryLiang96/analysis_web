# Create your models here.
import os

from django.conf import settings
from django.db import models


class Movie(models.Model):
    id = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=60)
    director = models.CharField(max_length=60)
    score = models.FloatField(default=0)
    poster = models.FilePathField(
        path=settings.POSTER_FILE_PATH_FIELD, blank=True)
    is_show = models.BooleanField(default=True)


class Comment(models.Model):
    username = models.CharField(max_length=60)
    star_rate = models.CharField(max_length=60)
    short_comment = models.TextField(blank=True)
    vote = models.IntegerField(default=0)
    time = models.DateField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Result(models.Model):
    comment_file = models.FilePathField(
        path=settings.COMMENT_FILE_PATH_FIELD, blank=True)
    comment_cut_file = models.FilePathField(
        path=settings.COMMENT_CUT_FILE_PATH_FIELD, blank=True)
    stop_word_file = models.FilePathField(
        path=settings.STOP_WORD_FILE_PATH_FIELD, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)