# Generated by Django 2.2.2 on 2020-02-13 12:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='export_data_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=50)),
                ('files_name', models.TextField(blank=True)),
                ('created_dt', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
