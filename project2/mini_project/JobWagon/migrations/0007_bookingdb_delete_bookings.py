# Generated by Django 5.1.5 on 2025-01-21 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobWagon', '0006_rename_booking_bookings'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('purpose', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('hours', models.PositiveIntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Bookings',
        ),
    ]
