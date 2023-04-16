# Generated by Django 4.2 on 2023-04-16 18:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("data_analysis", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="analysis",
            options={
                "verbose_name": "Строка данных",
                "verbose_name_plural": "Строки данных",
            },
        ),
        migrations.AlterModelOptions(
            name="analysissumbydate",
            options={
                "ordering": ("date",),
                "verbose_name": "Расчетный тотал по дате",
                "verbose_name_plural": "Расчетные тоталы по дате",
            },
        ),
    ]
