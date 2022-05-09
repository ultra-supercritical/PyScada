# Generated by Django 2.2.8 on 2020-02-11 10:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pyscada', '0058_merge_20191206_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='protocol',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.DeviceProtocol'),
        ),
        migrations.AlterField(
            model_name='devicewritetask',
            name='variable',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='devicewritetask',
            name='variable_property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.VariableProperty'),
        ),
        migrations.AlterField(
            model_name='event',
            name='variable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='recordeddata',
            name='variable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='recordeddataold',
            name='variable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
        migrations.AlterField(
            model_name='recordedevent',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Event'),
        ),
        migrations.AlterField(
            model_name='variable',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Device'),
        ),
        migrations.AlterField(
            model_name='variableproperty',
            name='variable',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pyscada.Variable'),
        ),
    ]
