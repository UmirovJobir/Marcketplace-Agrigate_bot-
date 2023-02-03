# Generated by Django 4.1.5 on 2023-02-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_category_slug_remove_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.PositiveBigIntegerField(unique=True)),
                ('username', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
    ]
