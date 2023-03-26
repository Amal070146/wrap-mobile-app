# Generated by Django 4.0.4 on 2023-03-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0007_booking_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='WrapUser',
            fields=[
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=40)),
                ('photo', models.ImageField(default='profile_photos/profile_user.png', upload_to='profile_photos/')),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(default='null', max_length=50)),
                ('wrapid', models.AutoField(primary_key=True, serialize=False)),
                ('coins', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
