# Generated by Django 4.0.4 on 2022-07-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0015_gatepass_pass_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepass',
            name='in_date',
            field=models.CharField(default='not-set', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='gatepass',
            name='out_date',
            field=models.CharField(default='not-set', max_length=20, null=True),
        ),
    ]
