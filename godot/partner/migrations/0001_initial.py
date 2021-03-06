# Generated by Django 3.2.7 on 2021-09-27 14:02

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=30)),
                ('partner_gst', models.CharField(max_length=30)),
                ('partner_phone', models.IntegerField()),
                ('partner_email', models.EmailField(max_length=254)),
                ('agency_website', models.URLField()),
            ],
            options={
                'verbose_name': 'partner',
                'verbose_name_plural': 'partners',
                'db_table': 'partner',
            },
            managers=[
                ('partner_obj', django.db.models.manager.Manager()),
            ],
        ),
    ]
