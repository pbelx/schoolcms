# Generated by Django 3.2.16 on 2022-12-12 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_alter_presentstudents_classdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentstudents',
            name='classdate',
            field=models.DateField(default='1987/09/20'),
        ),
    ]
