# Generated by Django 3.2.8 on 2021-10-09 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costumers',
            new_name='Costumer',
        ),
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]