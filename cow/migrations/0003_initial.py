# Generated by Django 3.2.12 on 2022-09-12 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cow', '0002_delete_neck_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='cow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cow_num', models.CharField(max_length=50)),
                ('group', models.CharField(default='new_cow', max_length=50)),
                ('stats', models.CharField(max_length=50)),
                ('carving_num', models.IntegerField(default=0)),
                ('age', models.IntegerField()),
                ('postpartal_days', models.IntegerField()),
                ('empyt_days', models.IntegerField()),
                ('birthday', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='estrus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('after_estrus', models.IntegerField()),
                ('after_fertilization', models.IntegerField()),
                ('estrus_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pre_childbirth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancy_days', models.IntegerField()),
                ('pre_childbirth', models.DateTimeField()),
                ('fertilization_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fertilization_num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_time', models.DateTimeField()),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cow.cow')),
            ],
        ),
        migrations.AddField(
            model_name='cow',
            name='childbirth_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cow.pre_childbirth'),
        ),
        migrations.AddField(
            model_name='cow',
            name='estrus_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cow.estrus'),
        ),
        migrations.AddField(
            model_name='cow',
            name='sensor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cow.sensor'),
        ),
    ]
