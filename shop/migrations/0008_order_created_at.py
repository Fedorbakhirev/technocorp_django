# Generated by Django 3.2.9 on 2021-11-18 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20211118_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateField(auto_created=True, null=True, verbose_name='Дата заказа'),
        ),
    ]
