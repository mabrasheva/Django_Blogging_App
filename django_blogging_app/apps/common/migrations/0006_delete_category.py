# Generated by Django 4.2.3 on 2023-07-25 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_remove_category_articles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]