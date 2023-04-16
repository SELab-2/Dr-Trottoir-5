# Generated by Django 4.1.7 on 2023-04-16 21:33

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("ronde", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="building",
            name="remarks",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.TextField(), default=list, size=None
            ),
        ),
        migrations.AddField(
            model_name="building",
            name="special_actions",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="building",
            name="manual",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="ronde.manual",
            ),
        ),
        migrations.AlterField(
            model_name="ronde",
            name="buildings",
            field=models.ManyToManyField(blank=True, to="ronde.building"),
        ),
    ]
