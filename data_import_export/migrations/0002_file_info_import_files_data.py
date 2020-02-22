# Generated by Django 2.2.2 on 2020-02-14 07:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200205_0603'),
        ('data_import_export', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='import_files_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files_name', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.AR_organization')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_import_data', to='account.Ar_user')),
            ],
        ),
        migrations.CreateModel(
            name='file_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.TextField()),
                ('file_data', models.TextField()),
                ('error_log', models.FileField(upload_to='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_by_file_info', to='account.Ar_user')),
            ],
        ),
    ]