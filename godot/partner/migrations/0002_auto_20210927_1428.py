# Generated by Django 3.2.7 on 2021-09-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='partner_gst',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='partner',
            name='partner_name',
            field=models.CharField(max_length=100),
        ),
    ]
