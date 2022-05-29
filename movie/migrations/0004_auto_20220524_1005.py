# Generated by Django 3.2.6 on 2022-05-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_book_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sorename', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('number', models.PositiveIntegerField(default=9983333333)),
            ],
            options={
                'verbose_name': 'AccountInfo',
                'verbose_name_plural': 'AccountInfos',
            },
        ),
        migrations.AlterField(
            model_name='book',
            name='time',
            field=models.CharField(max_length=50),
        ),
    ]
