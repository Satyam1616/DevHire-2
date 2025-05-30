# Generated by Django 5.1.4 on 2025-01-11 14:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dev', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('industry', models.CharField(blank=True, max_length=100)),
                ('website', models.URLField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.PositiveIntegerField(help_text='Duration in hours')),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('completed', 'Completed')], default='open', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_developer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='dev.profile')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customerprofile')),
                ('required_skills', models.ManyToManyField(to='dev.skill')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('message', models.TextField(help_text='Message to the customer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='customer.project')),
            ],
            options={
                'unique_together': {('project', 'developer')},
            },
        ),
        migrations.AddField(
            model_name='project',
            name='interested_developers',
            field=models.ManyToManyField(related_name='interested_projects', through='customer.ProjectRequest', to='dev.profile'),
        ),
        migrations.CreateModel(
            name='DeveloperRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('message', models.TextField(help_text='Message to the developer')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customerprofile')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dev.profile')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.project')),
            ],
            options={
                'unique_together': {('project', 'developer', 'customer')},
            },
        ),
    ]
