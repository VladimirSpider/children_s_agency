# Generated by Django 3.1.5 on 2021-03-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_for_project', '0004_auto_20210314_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='img_service1',
            field=models.ImageField(blank=True, upload_to='static/data_for_project/img/img_goods', verbose_name='Изображение услуги'),
        ),
    ]
