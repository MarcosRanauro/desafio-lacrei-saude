# Generated by Django 5.0 on 2023-12-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("consultas", "0005_rename_data_consulta_data_consulta"),
    ]

    operations = [
        migrations.AlterField(
            model_name="consulta",
            name="data_consulta",
            field=models.DateField(),
        ),
    ]