# Generated by Django 3.2.9 on 2022-01-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20211108_2201'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Library',
        ),
        migrations.AlterField(
            model_name='board',
            name='category',
            field=models.CharField(choices=[('공지사항', '공지사항')], default='News', max_length=10, verbose_name='카테고리'),
        ),
    ]
