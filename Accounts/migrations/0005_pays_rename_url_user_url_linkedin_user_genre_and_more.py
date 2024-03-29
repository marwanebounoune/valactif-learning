# Generated by Django 4.0.5 on 2022-06-17 16:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_delete_document_alter_user_options_alter_user_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'Pays',
            },
        ),
        migrations.RenameField(
            model_name='user',
            old_name='url',
            new_name='url_linkedIn',
        ),
        migrations.AddField(
            model_name='user',
            name='genre',
            field=models.CharField(blank=True, choices=[('1', 'Femme'), ('2', 'Homme')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lecons',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(null=True), size=None), blank=True, null=True, size=None), blank=True, null=True, size=None),
        ),
        migrations.CreateModel(
            name='Villes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.pays')),
            ],
            options={
                'db_table': 'Villes',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='pays',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.pays'),
        ),
        migrations.AddField(
            model_name='user',
            name='ville',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.villes'),
        ),
    ]
