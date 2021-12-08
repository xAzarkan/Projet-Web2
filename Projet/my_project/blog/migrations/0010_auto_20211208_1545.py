# Generated by Django 3.2.8 on 2021-12-08 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_map'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Map',
        ),
        migrations.AddField(
            model_name='post',
            name='address',
            field=models.TextField(default='Rue des fruits 4'),
        ),
        migrations.AddField(
            model_name='post',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='long',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
