# Generated by Django 4.0.4 on 2023-03-26 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0013_booking_uid_alter_booking_booking_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
    ]
