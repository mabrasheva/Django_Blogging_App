# Generated by Django 4.2.3 on 2023-07-25 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('article', '0005_alter_article_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='category.category'),
        ),
    ]
