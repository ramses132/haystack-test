# Generated by Django 2.0.3 on 2018-03-28 22:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='created_on',
        ),
    ]
