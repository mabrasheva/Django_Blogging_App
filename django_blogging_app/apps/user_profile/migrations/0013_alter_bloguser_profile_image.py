# Generated by Django 4.2.3 on 2023-07-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_alter_bloguser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloguser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]