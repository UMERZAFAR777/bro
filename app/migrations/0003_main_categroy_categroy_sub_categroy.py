# Generated by Django 5.0 on 2024-02-11 07:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_categroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.main_categroy')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Categroy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('categroy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.categroy')),
            ],
        ),
    ]
