# Generated by Django 5.1.6 on 2025-05-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlternativeSora', '0003_alter_mediaalternative_tb_namealternative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediaalternative_tb',
            name='authorAlternative',
            field=models.CharField(max_length=250, verbose_name='Author Alternative'),
        ),
    ]
