# Generated by Django 5.1.2 on 2024-10-24 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_price'),
        ('profiles', '0002_alter_profile_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='profiles.profile'),
        ),
    ]