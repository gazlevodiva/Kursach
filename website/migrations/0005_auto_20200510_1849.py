# Generated by Django 2.1.7 on 2020-05-10 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20200510_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.CharField(default='active', max_length=50),
        ),
    ]
