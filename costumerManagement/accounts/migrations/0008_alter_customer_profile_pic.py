# Generated by Django 3.2.8 on 2021-10-28 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic.jpg', null=True, upload_to=''),
        ),
    ]
