# Generated by Django 3.1.4 on 2022-01-28 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('experience', models.CharField(max_length=200, verbose_name='Experience')),
                ('description', models.TextField(null=True, verbose_name='Description')),
                ('organization', models.CharField(max_length=200, verbose_name='Organization')),
                ('address', models.TextField(null=True, verbose_name='Address')),
                ('email', models.CharField(max_length=1000, null=True, verbose_name='Link')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('name', models.CharField(max_length=50, verbose_name='CV Name')),
                ('file', models.FileField(max_length=1000, upload_to='uploads/document/cover_letters/')),
                ('text', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('middle_name', models.CharField(max_length=50, verbose_name='Middle Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('name', models.CharField(max_length=500, verbose_name='Qualification')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.jobprofile')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('name', models.CharField(max_length=500, verbose_name='Attribute')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.jobprofile')),
            ],
            options={
                'ordering': ('id',),
                'abstract': False,
            },
        ),
    ]