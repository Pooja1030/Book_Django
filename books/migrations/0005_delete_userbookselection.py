# Generated by Django 5.1 on 2024-09-03 05:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_userbookselection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserBookSelection',
        ),
    ]
