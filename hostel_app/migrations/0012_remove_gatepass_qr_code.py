# Generated by Django 4.0.4 on 2022-07-03 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0011_gatepass_qr_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='qr_code',
        ),
    ]