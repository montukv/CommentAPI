# Generated by Django 3.2.5 on 2021-07-01 11:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0002_rename_commentsdeta_commentsdata'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentsData',
            new_name='UserComment',
        ),
    ]
