# Generated by Django 2.2.2 on 2020-02-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_story_view', '0004_auto_20200205_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ar_user_story',
            name='ac_readability_score',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='ar_user_story',
            name='convo_readability_score',
            field=models.FloatField(blank=True),
        ),
    ]