# Generated by Django 4.0.4 on 2022-07-02 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0008_gatepass_student_data_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='in_time',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='issue_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='out_time',
            field=models.CharField(default='', max_length=20),
        ),
    ]
