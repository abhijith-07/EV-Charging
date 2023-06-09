# Generated by Django 4.2.1 on 2023-05-17 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("maps", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chargingstation",
            name="charger_type",
            field=models.CharField(
                choices=[
                    ("Level 1 Charging", "Level 1 Charging"),
                    ("Level 2 Charging", "Level 2 Charging"),
                    ("DC Fast Charging", "DC Fast Charging"),
                ],
                default="Level 1 Charging",
                max_length=125,
            ),
        ),
    ]
