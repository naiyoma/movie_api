# Generated by Django 4.0.4 on 2022-05-03 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_movie_rename_regular_movietype_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='no-image', upload_to='photos'),
        ),
    ]