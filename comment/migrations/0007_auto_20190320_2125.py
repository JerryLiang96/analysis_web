# Generated by Django 2.1.7 on 2019-03-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_auto_20190320_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FilePathField(blank=True, match='bo.jpg', path='/static/image/poster'),
        ),
    ]
