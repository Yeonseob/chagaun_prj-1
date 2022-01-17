# Generated by Django 3.2.9 on 2021-11-08 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('solution', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='구매일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='expired_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='만기일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='idfunnel_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='아이디퍼널 만기일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='shopfinder_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='쇼핑몰파인더 만기일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='snsfinder_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='SNS파인더 만기일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='갱신일'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]