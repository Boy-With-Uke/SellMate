# Generated by Django 5.0.2 on 2024-03-02 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_order_order_ordered_remove_cart_ordered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.SlugField(max_length=128)),
                ('price_promo', models.FloatField(default=0.0)),
                ('price', models.FloatField(default=0.0)),
                ('description', models.TextField(blank=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='promo')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.type')),
            ],
        ),
    ]
