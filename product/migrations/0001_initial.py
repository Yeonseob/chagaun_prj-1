# Generated by Django 2.1.1 on 2020-06-18 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, verbose_name='이름')),
                ('expired', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(12), django.core.validators.MinValueValidator(1)], verbose_name='기간(월)')),
                ('price', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000000), django.core.validators.MinValueValidator(0)], verbose_name='가격')),
            ],
        ),
    ]
