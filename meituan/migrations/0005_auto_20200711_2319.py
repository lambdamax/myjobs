# Generated by Django 2.1.8 on 2020-07-11 23:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meituan', '0004_auto_20200711_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='center',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='index',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='meituan.Index'),
        ),
    ]
