# Generated by Django 4.1.4 on 2022-12-15 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_area_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_area', to='hotel.area')),
            ],
        ),
    ]