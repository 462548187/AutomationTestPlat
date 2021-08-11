# Generated by Django 3.1.7 on 2021-08-04 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('image', models.ImageField(upload_to='', verbose_name='图片')),
                ('type', models.SmallIntegerField(choices=[(3, 'other'), (2, 'background'), (1, 'icon')], default=3, verbose_name='图片类型')),
                ('location', models.CharField(max_length=20, unique=True, verbose_name='使用位置')),
            ],
            options={
                'verbose_name': '系统图片',
                'verbose_name_plural': '系统图片',
                'db_table': 'tp_image',
            },
        ),
    ]
