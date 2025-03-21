# Generated by Django 5.1.6 on 2025-03-08 01:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_id', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('is_registered', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number', models.CharField(max_length=20, unique=True)),
                ('previous_roll_number', models.CharField(blank=True, max_length=20, null=True)),
                ('student_type', models.CharField(choices=[('regular', 'Regular'), ('lateral', 'Lateral'), ('rejoin', 'Rejoin')], max_length=10)),
                ('previous_student_type', models.CharField(blank=True, choices=[('regular', 'Regular'), ('lateral', 'Lateral'), ('rejoin', 'Rejoin')], max_length=10, null=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('rejoin_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('is_registered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='StaffPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('staff', 'Staff')], max_length=10)),
                ('password_hash', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('identifier', 'role')},
            },
        ),
        migrations.CreateModel(
            name='StudentPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=20)),
                ('role', models.CharField(choices=[('student', 'Student')], max_length=10)),
                ('password_hash', models.CharField(max_length=255)),
                ('salt', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'unique_together': {('identifier', 'role')},
            },
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=64, unique=True)),
                ('user_id', models.IntegerField()),
                ('user_type', models.CharField(max_length=10)),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('expires_at', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('last_used', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user_sessions',
                'indexes': [models.Index(fields=['session_id'], name='user_sessio_session_e62ba3_idx'), models.Index(fields=['user_id'], name='user_sessio_user_id_eb20aa_idx'), models.Index(fields=['user_type'], name='user_sessio_user_ty_342aed_idx')],
            },
        ),
    ]
