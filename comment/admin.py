from django.contrib import admin
from .models import Comment, Movie, Result
# Register your models here.


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'poster', 'is_show')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'username', 'vote')


@admin.register(Result)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_id', 'comment_file', 'comment_cut_file')
