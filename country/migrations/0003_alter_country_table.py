# Generated by Django 5.1.4 on 2024-12-20 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0002_alter_country_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='country',
            table='countries',
        ),
    ]