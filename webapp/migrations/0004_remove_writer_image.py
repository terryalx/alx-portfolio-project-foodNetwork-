# Generated by Django 5.0.1 on 2024-01-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_delete_subscriber'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='image',
        ),
    ]
