# Generated by Django 4.2.2 on 2023-07-11 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('odmapp', '0002_donar_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donar',
            name='user',
        ),
    ]
