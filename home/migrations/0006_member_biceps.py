# Generated by Django 4.2.3 on 2023-12-10 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='biceps',
            field=models.CharField(default='kbk,', max_length=10),
        ),
    ]