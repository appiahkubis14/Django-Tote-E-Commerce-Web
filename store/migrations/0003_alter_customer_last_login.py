# Generated by Django 5.1.4 on 2025-01-05 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_date_joined_customer_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]