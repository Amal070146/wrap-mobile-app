# Generated by Django 4.0.4 on 2023-03-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0012_booking_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='uid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='booking_address',
            field=models.CharField(default='null', max_length=100),
        ),
        migrations.AlterField(
            model_name='booking',
            name='typeaddress',
            field=models.CharField(max_length=100),
        ),
    ]
