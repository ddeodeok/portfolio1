# Generated by Django 3.2.12 on 2022-09-12 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0004_auto_20220912_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cow',
            name='childbirth_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cow.pre_childbirth'),
        ),
        migrations.AlterField(
            model_name='cow',
            name='estrus_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cow.estrus'),
        ),
        migrations.AlterField(
            model_name='cow',
            name='postpartal_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cow',
            name='sensor_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cow.sensor'),
        ),
    ]
