# Generated by Django 4.0.4 on 2023-03-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0014_remove_booking_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='date',
            field=models.DateField(verbose_name='Y-m-d'),
        ),
    ]
