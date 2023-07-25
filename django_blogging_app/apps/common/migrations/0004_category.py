# Generated by Django 4.2.3 on 2023-07-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_alter_article_user'),
        ('common', '0003_alter_comment_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('articles', models.ManyToManyField(to='article.article')),
            ],
        ),
    ]
