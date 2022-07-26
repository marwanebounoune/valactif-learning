# Generated by Django 4.0.5 on 2022-07-25 16:11

import django.contrib.auth.models
import django.contrib.auth.validators
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('photoProfile', models.FileField(blank=True, null=True, upload_to='images/profiles/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg', 'tiff'])])),
                ('tel1', models.CharField(blank=True, max_length=13, null=True)),
                ('dateNaissance', models.CharField(blank=True, max_length=1, null=True)),
                ('adresse', models.CharField(blank=True, max_length=500, null=True)),
                ('url_linkedIn', models.CharField(blank=True, max_length=500, null=True)),
                ('genre', models.CharField(blank=True, choices=[('1', 'Femme'), ('2', 'Homme')], max_length=1, null=True)),
                ('lecons', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None), blank=True, null=True, size=None)),
                ('is_connected', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('pays', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.pays')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('ville', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.villes')),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
