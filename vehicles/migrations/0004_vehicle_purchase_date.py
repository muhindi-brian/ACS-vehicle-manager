# Generated by Django 5.1.3 on 2024-11-21 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0003_maintenance_mileage_vehicle_mileage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='purchase_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
