# Generated by Django 3.2.6 on 2022-05-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220525_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(default=' ', max_length=20),
        ),
    ]
