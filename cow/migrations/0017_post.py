# Generated by Django 3.2.12 on 2022-09-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0016_auto_20220914_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
    ]
