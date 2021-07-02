# Generated by Django 3.2.5 on 2021-07-02 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0009_alter_usercomment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercomment',
            old_name='comments',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='page',
            name='slug',
            field=models.CharField(max_length=300),
        ),
    ]