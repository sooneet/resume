# Generated by Django 3.2 on 2022-04-09 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_rename_professional_experience_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('service_images', models.ImageField(upload_to='')),
                ('service_title', models.CharField(max_length=50)),
                ('service_details', models.TextField()),
            ],
        ),
    ]
