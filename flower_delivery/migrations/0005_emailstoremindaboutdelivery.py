# Generated by Django 4.2.4 on 2023-09-01 14:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("flower_delivery", "0004_callme"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmailsToRemindAboutDelivery",
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
                ("email", models.CharField(max_length=60)),
            ],
        ),
    ]
