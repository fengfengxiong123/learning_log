# Generated by Django 2.1.4 on 2019-05-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_type',
            field=models.CharField(max_length=200, verbose_name='主题'),
        ),
    ]
