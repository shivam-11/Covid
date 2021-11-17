# Generated by Django 3.1.1 on 2021-08-30 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('age', models.IntegerField()),
                ('phone_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('x_ray_image', models.ImageField(default='', upload_to='CovidPrediction/images')),
                ('covid_status', models.CharField(max_length=10)),
            ],
        ),
    ]
