# Generated by Django 4.0.4 on 2022-07-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0010_gatepass_hex_code_alter_gatepass_in_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepass',
            name='qr_code',
            field=models.ImageField(default=' ', upload_to='qr_code'),
        ),
    ]
