# Generated by Django 5.1.5 on 2025-02-22 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_complaint',
            name='complaint_id',
        ),
    ]
