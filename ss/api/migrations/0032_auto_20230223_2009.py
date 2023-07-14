# Generated by Django 3.2.16 on 2023-02-23 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0031_subjectteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectteacher',
            name='subjectName',
            field=models.ForeignKey(db_column='subjectName', on_delete=django.db.models.deletion.CASCADE, to='api.subjects'),
        ),
        migrations.AlterField(
            model_name='subjectteacher',
            name='subjectTeacher',
            field=models.ForeignKey(db_column='firstname', on_delete=django.db.models.deletion.CASCADE, to='api.teachers'),
        ),
    ]
