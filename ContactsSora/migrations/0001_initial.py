# Generated by Django 5.1.6 on 2025-03-12 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoryAR_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleCat', models.CharField(max_length=150, verbose_name='Title Net')),
            ],
        ),
        migrations.CreateModel(
            name='AttentionRoute_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('whatsappAR', models.CharField(max_length=30, null=True, verbose_name='Whatsapp AR')),
                ('phoneAR', models.CharField(max_length=35, null=True, verbose_name='Phone AR')),
                ('locationAR', models.CharField(max_length=250, null=True, verbose_name='Location AR')),
                ('titleCat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContactsSora.categoryar_tb')),
            ],
        ),
    ]
