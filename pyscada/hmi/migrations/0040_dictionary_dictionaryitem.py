# Generated by Django 2.2.8 on 2020-10-02 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hmi', '0039_auto_20201002_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='DictionaryItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('label', models.CharField(default='', max_length=400)),
                ('value', models.CharField(default='', max_length=400)),
                ('dictionary', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hmi.Dictionary')),
            ],
        ),
    ]
