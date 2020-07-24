# Generated by Django 2.2.5 on 2020-07-24 18:19

from django.db import migrations, models
import modelos.validators


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0005_auto_20200611_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cnnmodel',
            name='normalize_mean',
            field=models.CharField(default='120.602, 147.384, 130.222', max_length=100, validators=[modelos.validators.check_output_tuple_normalized_values]),
        ),
        migrations.AlterField(
            model_name='cnnmodel',
            name='normalize_std',
            field=models.CharField(default='50.602, 47.384, 30.222', max_length=100, validators=[modelos.validators.check_output_tuple_normalized_values]),
        ),
    ]
