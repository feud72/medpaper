# Generated by Django 2.0.5 on 2018-05-31 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubmed_api', '0004_auto_20180531_1657'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pubmedapi',
            name='id',
        ),
        migrations.AlterField(
            model_name='pubmedapi',
            name='name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='NAME'),
        ),
    ]
