# Generated by Django 4.0.5 on 2022-06-20 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0006_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]