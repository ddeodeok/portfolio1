# Generated by Django 3.2.12 on 2022-09-12 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0012_delete_sensor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='cid',
        ),
        migrations.DeleteModel(
            name='Cow',
        ),
        migrations.DeleteModel(
            name='Estrus',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Pre_childbirth',
        ),
    ]
