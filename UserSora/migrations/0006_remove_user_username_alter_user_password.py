# Generated by Django 5.1.6 on 2025-03-04 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSora', '0005_alter_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=300, verbose_name='User Password'),
        ),
    ]
