# Generated by Django 2.2.2 on 2020-02-05 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_story_view', '0003_auto_20200205_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_user_story',
            name='owner',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Ar_user'),
        ),
    ]
