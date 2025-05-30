# Generated by Django 5.1.6 on 2025-04-08 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSora', '0007_remove_user_contactnumber_remove_user_fullname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ageUser_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ageUser', models.CharField(max_length=255, verbose_name='Age User')),
            ],
        ),
        migrations.CreateModel(
            name='educationLevelUser_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educationUser', models.CharField(max_length=255, verbose_name='Education User')),
            ],
        ),
        migrations.CreateModel(
            name='rangeSalary_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salaryUser', models.CharField(max_length=255, verbose_name='Salary User')),
            ],
        ),
        migrations.CreateModel(
            name='relationKindUser_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationUser', models.CharField(max_length=255, verbose_name='Relation User')),
            ],
        ),
        migrations.CreateModel(
            name='workUser_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workUser', models.CharField(max_length=255, verbose_name='Work User')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='educationLevel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='haveKids',
        ),
        migrations.RemoveField(
            model_name='user',
            name='relationKind',
        ),
        migrations.RemoveField(
            model_name='user',
            name='salaryRange',
        ),
        migrations.RemoveField(
            model_name='user',
            name='workSituation',
        ),
        migrations.AddField(
            model_name='user',
            name='ageUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSora.ageuser_tb'),
        ),
        migrations.AddField(
            model_name='user',
            name='educationUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSora.educationleveluser_tb'),
        ),
        migrations.AddField(
            model_name='user',
            name='salaryUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSora.rangesalary_tb'),
        ),
        migrations.AddField(
            model_name='user',
            name='relationUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSora.relationkinduser_tb'),
        ),
        migrations.AddField(
            model_name='user',
            name='workUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='UserSora.workuser_tb'),
        ),
    ]
