# Generated by Django 4.0.4 on 2022-07-11 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0017_gatepass_my_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gatepass',
            name='my_check',
        ),
    ]
