# Generated by Django 2.2.7 on 2020-04-04 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0016_auto_20200402_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=None, max_length=100)),
                ('component_name', models.CharField(default=None, max_length=500)),
                ('component_quantity', models.CharField(default=None, max_length=500)),
                ('component_cost', models.CharField(default=None, max_length=500)),
            ],
        ),
    ]
