# Generated by Django 5.1.7 on 2025-03-26 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
