# Generated by Django 4.2.3 on 2023-12-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_member_join_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateTimeField(),
        ),
    ]
