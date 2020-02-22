# Generated by Django 2.2.4 on 2020-01-09 05:55

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArUserStoryPoints',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('very_small', models.BigIntegerField(default=0)),
                ('smallish', models.BigIntegerField(default=0)),
                ('small', models.BigIntegerField(default=0)),
                ('medium', models.BigIntegerField(default=0)),
                ('large', models.BigIntegerField(default=0)),
                ('extra_large', models.BigIntegerField(default=0)),
                ('extra_extra_large', models.BigIntegerField(default=0)),
                ('extra_extra_extra_large', models.BigIntegerField(default=0)),
                ('epic', models.BigIntegerField(default=0)),
                ('create_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_dt', models.DateTimeField(default=django.utils.timezone.now)),
                ('ORG_ID', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='account.AR_organization')),
                ('create_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='create_by_stroypoints', to='account.Ar_user')),
                ('update_by', models.ForeignKey(on_delete='models.SET_NULL', related_name='update_by_storypoints', to='account.Ar_user')),
            ],
        ),
    ]
