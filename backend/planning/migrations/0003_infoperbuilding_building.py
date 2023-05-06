# Generated by Django 4.2 on 2023-05-02 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ronde", "0004_building_syndicus"),
        ("planning", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="infoperbuilding",
            name="building",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ronde.building",
            ),
        ),
    ]
