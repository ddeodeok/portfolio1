# Generated by Django 3.2.12 on 2022-09-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0021_auto_20220914_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cow',
            name='childbirth_id',
        ),
        migrations.RemoveField(
            model_name='cow',
            name='estrus_id',
        ),
        migrations.AlterField(
            model_name='cow',
            name='birthday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]