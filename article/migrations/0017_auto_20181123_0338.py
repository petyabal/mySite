# Generated by Django 2.1.2 on 2018-11-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20181123_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_submission',
            field=models.TextField(max_length=350, verbose_name='Краткое изложение'),
        ),
    ]
