# Generated by Django 3.2.9 on 2021-11-08 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='method',
            field=models.TextField(default='', verbose_name='결제수단'),
        ),
    ]
