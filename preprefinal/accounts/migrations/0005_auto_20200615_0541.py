# Generated by Django 2.0.1 on 2020-06-15 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200614_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_name',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]