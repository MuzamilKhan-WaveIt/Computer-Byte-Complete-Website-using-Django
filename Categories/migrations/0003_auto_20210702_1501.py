# Generated by Django 3.1 on 2021-07-02 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_auto_20210702_1500'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CATEGORIES',
            new_name='CATEGORY',
        ),
    ]