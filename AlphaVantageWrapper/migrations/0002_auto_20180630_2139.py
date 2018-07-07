# Generated by Django 2.0.6 on 2018-06-30 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AlphaVantageWrapper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='functionparameter',
            name='id',
        ),
        migrations.AlterField(
            model_name='functionparameter',
            name='function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='AlphaVantageWrapper.Function'),
        ),
        migrations.AlterField(
            model_name='functionparameter',
            name='parameter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, to='AlphaVantageWrapper.Parameter'),
        ),
    ]