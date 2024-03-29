# Generated by Django 5.0.1 on 2024-03-20 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_remove_building_assigned_people_building_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='building',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.building'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='resources',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.people'),
        ),
    ]
