from django.shortcuts import render, redirect

# Create your views here.
import numpy as np
from .models import Movie, Comment
from django_pandas.io import read_frame
from django.contrib.auth.decorators import login_required


@login_required
def result(request, movie_id):
    # 电影信息数据
    movie = Movie.objects.get(id=movie_id)
    comments = Comment.objects.filter(movie_id=movie)
    # 最优及最差影评数据
    best_comment = comments.filter(star_rate='力荐').order_by('-vote').first
    worst_comment = comments.filter(star_rate='很差').order_by('-vote').first
    # 直方图数据
    label_list = ['力荐', '推荐', '还行', '较差', '很差']
    df = read_frame(comments)
    df = df[df.star_rate.isin(label_list)]
    count_df = df.groupby('star_rate')['vote'].count().to_frame()
    count_df['label'] = count_df.index
    count_df['label'] = count_df['label'].astype('category')
    count_df['label'].cat.reorder_categories(label_list, inplace=True)
    count_df.sort_values('label', inplace=True)
    count_df.rename(columns={'vote': 'count'}, inplace=True)
    # 散点图数据
    point_df = df[['star_rate', 'vote']]
    map_dict = dict(zip(label_list, range(5)))
    point_df['star_rate'].replace(map_dict, inplace=True)
    point_df['vote'] = point_df['vote'].apply(lambda x: int(pow(x, 3 / 7)) + 1)
    # 返回数据
    context = {}
    context['movie'] = movie
    context['label'] = count_df['label'].to_list()
    context['count'] = count_df['count'].to_list()
    context['point'] = point_df.values.tolist()
    context['best_comment'] = best_comment
    context['worst_comment'] = worst_comment
    return render(request, 'result.html', context)
