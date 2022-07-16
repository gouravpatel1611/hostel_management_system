# Generated by Django 4.0.4 on 2022-06-30 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel_app', '0002_student_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='username',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='parents_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='student_data',
            name='student_number',
            field=models.IntegerField(),
        ),
    ]
