# Generated by Django 5.1.5 on 2025-03-15 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0018_tbl_community_mentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_community',
            name='community_status',
            field=models.IntegerField(default=0),
        ),
    ]
