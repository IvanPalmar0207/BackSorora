# Generated by Django 5.1.6 on 2025-05-19 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactsSora', '0002_usercontactconfidence_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontactconfidence_tb',
            name='nameContact',
            field=models.CharField(default='', max_length=250, verbose_name='Name Contact'),
        ),
    ]
