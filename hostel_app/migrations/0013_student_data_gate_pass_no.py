# Generated by Django 4.0.4 on 2022-07-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0012_remove_gatepass_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='gate_pass_no',
            field=models.CharField(default='NO', max_length=10),
        ),
    ]
