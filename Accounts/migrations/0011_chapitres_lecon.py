# Generated by Django 4.0.5 on 2022-06-23 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0010_alter_chapitres_url_alter_lecons_url_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapitres',
            name='lecon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Accounts.lecons'),
            preserve_default=False,
        ),
    ]
