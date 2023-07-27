# Generated by Django 4.2.3 on 2023-07-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0014_alter_bloguser_profile_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='profile_image',
        ),
        migrations.AddField(
            model_name='bloguser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
    ]