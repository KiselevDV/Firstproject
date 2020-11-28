# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-11-28 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название пиццы')),
                ('description', models.CharField(max_length=50, verbose_name='Краткое описвние')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='PizzaShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Пиццерия')),
                ('description', models.TextField(verbose_name='Описание')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
                ('url', models.URLField(verbose_name='Интернет-адрес пиццерии')),
            ],
            options={
                'verbose_name': 'Пиццеррия',
                'verbose_name_plural': 'Пиццерии',
            },
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizzashop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstapp.PizzaShop', verbose_name='Пиццерия'),
        ),
    ]
