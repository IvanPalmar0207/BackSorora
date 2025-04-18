# Generated by Django 5.0.4 on 2025-04-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSora', '0006_remove_user_username_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contactNumber',
        ),
        migrations.RemoveField(
            model_name='user',
            name='fullName',
        ),
        migrations.AddField(
            model_name='user',
            name='educationLevel',
            field=models.CharField(max_length=250, null=True, verbose_name='Education Level'),
        ),
        migrations.AddField(
            model_name='user',
            name='haveKids',
            field=models.BooleanField(max_length=250, null=True, verbose_name='Have Kids'),
        ),
        migrations.AddField(
            model_name='user',
            name='relationKind',
            field=models.CharField(max_length=250, null=True, verbose_name='Relation Kind'),
        ),
        migrations.AddField(
            model_name='user',
            name='salaryRange',
            field=models.CharField(max_length=250, null=True, verbose_name='Salary Range'),
        ),
        migrations.AddField(
            model_name='user',
            name='workSituation',
            field=models.CharField(max_length=250, null=True, verbose_name='Work Situation'),
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.CharField(max_length=250, null=True, verbose_name='User Age'),
        ),
    ]
