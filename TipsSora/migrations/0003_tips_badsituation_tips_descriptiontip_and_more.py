# Generated by Django 5.1.6 on 2025-04-01 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TipsSora', '0002_tips_nametip'),
    ]

    operations = [
        migrations.AddField(
            model_name='tips',
            name='badSituation',
            field=models.TextField(default=0, verbose_name='Bad Situation'),
        ),
        migrations.AddField(
            model_name='tips',
            name='descriptionTip',
            field=models.TextField(default=0, verbose_name='Description Field'),
        ),
        migrations.AddField(
            model_name='tips',
            name='goodSituation',
            field=models.TextField(default=0, verbose_name='Good Situation'),
        ),
    ]
