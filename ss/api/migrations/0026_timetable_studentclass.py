# Generated by Django 3.2.16 on 2023-01-10 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_auto_20230110_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='timetable',
            name='studentclass',
            field=models.CharField(choices=[('P1', 'P1'), ('P2', 'P2'), ('P3', 'P3'), ('P4', 'P4'), ('P5', 'P5'), ('P6', 'P6'), ('P7', 'P7')], default='P1', max_length=20),
        ),
    ]
