# Generated by Django 4.2 on 2023-07-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_bank', '0004_licence'),
    ]

    operations = [
        migrations.AddField(
            model_name='licence',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
