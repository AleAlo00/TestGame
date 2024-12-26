# Generated by Django 5.1.4 on 2024-12-26 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characteristics", "0001_initial"),
        ("phone", "0002_alter_myphone_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mycharacteristics",
            name="id_cell",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="phone.myphone"
            ),
        ),
    ]
