# Generated by Django 5.1.5 on 2025-02-28 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_tbl_category_tbl_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_name', models.CharField(max_length=30)),
            ],
        ),
    ]
