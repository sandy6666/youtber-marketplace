# Generated by Django 3.1.7 on 2021-03-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(default='#', max_length=255),
        ),
    ]
