# Generated by Django 2.0.5 on 2018-05-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed_api', '0006_auto_20180531_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pubmedapi',
            name='url',
            field=models.CharField(max_length=70, null=True, verbose_name='URL'),
        ),
    ]
