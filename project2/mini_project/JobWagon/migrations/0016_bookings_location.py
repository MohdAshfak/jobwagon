# Generated by Django 5.1.5 on 2025-01-22 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobWagon', '0015_bookings_reason'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookings',
            name='location',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
