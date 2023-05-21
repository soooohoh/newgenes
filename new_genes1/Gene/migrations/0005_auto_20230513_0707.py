# Generated by Django 2.2 on 2023-05-13 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0004_lifestyle'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='goals',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='intro',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics'),
        ),
    ]
