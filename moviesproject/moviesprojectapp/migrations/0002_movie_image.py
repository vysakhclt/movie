# Generated by Django 3.2 on 2021-04-19 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviesprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='img', upload_to='picture'),
            preserve_default=False,
        ),
    ]