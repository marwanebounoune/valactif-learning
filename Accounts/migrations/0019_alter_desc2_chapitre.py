# Generated by Django 4.0.5 on 2022-06-30 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0018_alter_lecons_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desc2',
            name='chapitre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.chapitres'),
        ),
    ]
