# Generated by Django 2.1.7 on 2019-03-20 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_movie_is_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FilePathField(path='/static/image/poster'),
        ),
    ]
