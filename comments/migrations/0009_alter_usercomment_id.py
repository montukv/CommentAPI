# Generated by Django 3.2.5 on 2021-07-02 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0008_auto_20210702_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercomment',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
