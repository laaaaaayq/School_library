# Generated by Django 4.2.5 on 2023-10-13 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='issue',
            name='returndate',
        ),
    ]
