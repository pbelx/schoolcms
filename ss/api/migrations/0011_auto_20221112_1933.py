# Generated by Django 3.2.16 on 2022-11-12 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_students_studentbirth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachers',
            old_name='name',
            new_name='firstname',
        ),
        migrations.AddField(
            model_name='teachers',
            name='address',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='contact',
            field=models.IntegerField(default=256444),
        ),
        migrations.AddField(
            model_name='teachers',
            name='email',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='maritals',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], default='single', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='nin',
            field=models.CharField(default='0', max_length=100),
        ),
        migrations.AddField(
            model_name='teachers',
            name='refcontact',
            field=models.CharField(default='former employer', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='refname',
            field=models.CharField(default='former empl', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='secondname',
            field=models.CharField(default='test', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teachers',
            name='title',
            field=models.CharField(choices=[('Mr', 'Mr'), ('Mrs', 'Mrs')], default='mr', max_length=3),
            preserve_default=False,
        ),
    ]
