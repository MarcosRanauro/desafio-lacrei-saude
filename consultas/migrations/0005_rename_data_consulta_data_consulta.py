# Generated by Django 4.2.7 on 2023-12-02 21:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("consultas", "0004_rename_data_consulta_consulta_data"),
    ]

    operations = [
        migrations.RenameField(
            model_name="consulta",
            old_name="data",
            new_name="data_consulta",
        ),
    ]
