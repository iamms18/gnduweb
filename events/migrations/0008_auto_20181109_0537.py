# Generated by Django 2.0.6 on 2018-11-09 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20181109_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='department_name',
            field=models.CharField(choices=[('BTECH-CSE', 'BTECH-CSE'), ('BTECH-CIVIL', 'BTECH-CIVIL'), ('BTECH-MECHANICAL', 'BTECH-MECHANICAL')], default='BTECH-CSE', max_length=70),
        ),
    ]
