# Generated by Django 5.1.4 on 2024-12-26 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("characteristics", "0002_alter_mycharacteristics_id_cell"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mycharacteristics",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
