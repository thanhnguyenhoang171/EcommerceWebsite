# Generated by Django 3.2.25 on 2024-09-25 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddress',
            name='order',
        ),
    ]