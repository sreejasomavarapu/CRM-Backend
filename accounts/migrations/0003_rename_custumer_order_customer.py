# Generated by Django 4.0 on 2022-06-12 05:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_costumer_order_custumer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='custumer',
            new_name='customer',
        ),
    ]
