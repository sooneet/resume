# Generated by Django 3.2 on 2022-04-09 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220409_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='summary',
            old_name='persone_email',
            new_name='person_email',
        ),
    ]
