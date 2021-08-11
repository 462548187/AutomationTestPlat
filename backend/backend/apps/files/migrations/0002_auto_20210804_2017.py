# Generated by Django 3.1.7 on 2021-08-04 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='type',
            field=models.SmallIntegerField(choices=[(1, 'icon'), (2, 'background'), (3, 'other')], default=3, verbose_name='图片类型'),
        ),
    ]