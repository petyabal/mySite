# Generated by Django 2.1.2 on 2018-11-21 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_auto_20181121_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_tegs',
            field=models.ManyToManyField(to='article.Tag', verbose_name='Теги'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='article.Category', verbose_name='Категория'),
        ),
    ]