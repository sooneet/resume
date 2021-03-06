# Generated by Django 2.2.16 on 2022-04-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_description', models.CharField(max_length=200)),
                ('profession_title', models.CharField(max_length=200)),
                ('profession_description', models.CharField(max_length=200)),
                ('birthday', models.DateField()),
                ('website', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('freelance', models.CharField(max_length=50)),
                ('profession_details', models.CharField(max_length=200)),
                ('about_pic', models.ImageField(upload_to='about_pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
