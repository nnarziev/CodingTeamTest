# Generated by Django 4.1.3 on 2022-11-28 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'verbose_name': 'Food', 'verbose_name_plural': 'Foods'},
        ),
        migrations.AlterModelOptions(
            name='foodcategory',
            options={'verbose_name': 'Food Category', 'verbose_name_plural': 'Food Categories'},
        ),
        migrations.AlterModelOptions(
            name='topping',
            options={'verbose_name': 'Topping', 'verbose_name_plural': 'Toppings'},
        ),
    ]
