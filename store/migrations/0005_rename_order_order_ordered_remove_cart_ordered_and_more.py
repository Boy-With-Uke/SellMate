# Generated by Django 5.0.2 on 2024-02-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order',
            new_name='ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered_date',
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
