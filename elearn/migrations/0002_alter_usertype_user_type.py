# Generated by Django 4.1.3 on 2022-11-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertype',
            name='user_type',
            field=models.CharField(default='admin', max_length=20),
        ),
    ]