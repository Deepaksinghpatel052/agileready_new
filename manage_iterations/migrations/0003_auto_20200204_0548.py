# Generated by Django 2.2.2 on 2020-02-04 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_iterations', '0002_auto_20200204_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ariterations',
            name='EndDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='ariterations',
            name='StartDate',
            field=models.DateTimeField(),
        ),
    ]
