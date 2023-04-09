# Generated by Django 4.1.4 on 2023-04-07 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Students",
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
                ("first_name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("roll_number", models.IntegerField()),
                ("mobile", models.CharField(max_length=10)),
            ],
        ),
    ]
