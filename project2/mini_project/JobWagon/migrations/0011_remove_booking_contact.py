# Generated by Django 5.1.5 on 2025-01-21 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('JobWagon', '0010_alter_booking_contact_alter_booking_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='contact',
        ),
    ]
