# Generated by Django 5.1.1 on 2024-09-25 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_delete_userbookselection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='price',
        ),
    ]