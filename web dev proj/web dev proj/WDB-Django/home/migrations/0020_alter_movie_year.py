# Generated by Django 4.0.4 on 2022-10-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_movie_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(default='2000', max_length=4),
        ),
    ]
