# Generated by Django 3.2 on 2022-04-09 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_fact_fact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fact',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='hard_workers',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='hours_of_support',
        ),
        migrations.RemoveField(
            model_name='fact',
            name='projects',
        ),
        migrations.AddField(
            model_name='fact',
            name='fact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='fact',
            name='fact_value',
            field=models.IntegerField(null=True),
        ),
    ]