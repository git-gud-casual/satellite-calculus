# Generated by Django 3.2.5 on 2023-10-26 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0003_auto_20231026_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='SatellitePictureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(blank=True, max_length=256, null=True)),
                ('lat_1', models.FloatField(null=True)),
                ('lon_1', models.FloatField(null=True)),
                ('lat_2', models.FloatField(null=True)),
                ('lon_2', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='expiration_date',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='lat_1',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='lat_2',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='lon_1',
        ),
        migrations.RemoveField(
            model_name='picturemodel',
            name='lon_2',
        ),
        migrations.AddField(
            model_name='picturemodel',
            name='url',
            field=models.ImageField(max_length=256, null=True, upload_to='pictures/'),
        ),
        migrations.AlterField(
            model_name='picturemodel',
            name='link',
            field=models.CharField(max_length=256, null=True),
        ),
    ]