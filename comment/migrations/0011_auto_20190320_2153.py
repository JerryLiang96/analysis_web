# Generated by Django 2.1.7 on 2019-03-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0010_auto_20190320_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FilePathField(blank=True, path='C:/Users/lzr/analysis_web/static/image/poster'),
        ),
    ]