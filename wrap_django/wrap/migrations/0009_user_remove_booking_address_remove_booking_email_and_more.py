# Generated by Django 4.0.4 on 2023-03-26 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wrap', '0008_wrapuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=40, unique=True)),
                ('photo', models.ImageField(default='profile_photos/profile_user.png', upload_to='profile_photos/')),
                ('password', models.CharField(max_length=20)),
                ('address', models.CharField(default='null', max_length=50)),
                ('coins', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='booking',
            name='address',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='email',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='password',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='wrapuser',
            name='address',
        ),
        migrations.RemoveField(
            model_name='wrapuser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='wrapuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='wrapuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='wrapuser',
            name='photo',
        ),
        migrations.AlterField(
            model_name='wrapuser',
            name='coins',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='uid',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='wrap.user'),
        ),
    ]
