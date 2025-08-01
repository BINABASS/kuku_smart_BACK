# Generated by Django 4.2.7 on 2025-07-23 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("breeds", "0001_initial"),
        ("batches", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="batchactivity",
            name="breed_activity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="breeds.breedactivity"
            ),
        ),
        migrations.AddField(
            model_name="batch",
            name="breed",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="breeds.breed"
            ),
        ),
    ]
