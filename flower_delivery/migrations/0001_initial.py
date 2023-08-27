# Generated by Django 4.2.4 on 2023-08-27 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flower",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("flower_name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images")),
            ],
        ),
        migrations.CreateModel(
            name="FlowerVariant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("variant_of_flower", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="images")),
                ("price", models.IntegerField(default=0)),
                (
                    "flower",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flower_delivery.flower",
                    ),
                ),
            ],
        ),
    ]
