# Generated by Django 5.1.5 on 2025-02-22 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_id', models.CharField(max_length=30)),
                ('complaint_title', models.CharField(max_length=30)),
                ('complaint_content', models.CharField(max_length=30)),
                ('complaint_replay', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
