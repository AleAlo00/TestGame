# Generated by Django 5.1.4 on 2024-12-30 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('phone', '0004_myphone_haracteristics'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myphone',
            old_name='haracteristics',
            new_name='characteristics',
        ),
    ]