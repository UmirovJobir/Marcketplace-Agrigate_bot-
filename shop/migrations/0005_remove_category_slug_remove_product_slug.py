# Generated by Django 4.1.5 on 2023-02-02 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]
