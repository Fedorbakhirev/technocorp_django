# Generated by Django 3.2.9 on 2021-11-18 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20211118_2220'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='customer_username',
            field=models.CharField(max_length=255, null=True, verbose_name='Логин покупателя'),
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.TextField(null=True, verbose_name='Товары'),
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
