# Generated by Django 2.1.4 on 2019-05-28 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_auto_20190528_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='art_name',
            field=models.CharField(max_length=200, verbose_name='标题'),
        ),
    ]
