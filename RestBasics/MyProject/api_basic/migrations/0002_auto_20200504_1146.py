# Generated by Django 3.0.6 on 2020-05-04 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Author',
            new_name='Article',
        ),
    ]