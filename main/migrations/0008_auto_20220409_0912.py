# Generated by Django 3.2 on 2022-04-09 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_skill_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fact', models.CharField(max_length=50)),
                ('clients', models.IntegerField()),
                ('projects', models.IntegerField()),
                ('hours_of_support', models.IntegerField()),
                ('hard_workers', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='about_pic',
            field=models.ImageField(upload_to=''),
        ),
    ]
