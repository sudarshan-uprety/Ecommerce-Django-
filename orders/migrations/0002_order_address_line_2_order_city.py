# Generated by Django 4.1.7 on 2023-04-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address_line_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]