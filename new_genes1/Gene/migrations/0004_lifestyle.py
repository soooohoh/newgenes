# Generated by Django 2.2 on 2023-05-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gene', '0003_delete_lifestyle'),
    ]

    operations = [
        migrations.CreateModel(
            name='LifeStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gene_name', models.CharField(max_length=20)),
                ('style', models.TextField()),
            ],
        ),
    ]
