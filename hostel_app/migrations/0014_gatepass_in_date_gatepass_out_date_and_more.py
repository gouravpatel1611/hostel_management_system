# Generated by Django 4.0.4 on 2022-07-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0013_student_data_gate_pass_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatepass',
            name='in_date',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='gatepass',
            name='out_date',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='in_time',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='out_time',
            field=models.CharField(default=' ', max_length=20, null=True),
        ),
    ]
