# Generated by Django 4.0.4 on 2022-06-22 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0012_alter_homework_author_alter_task_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='razdel',
            name='image',
            field=models.ImageField(upload_to='edu', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='razdel',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название раздела'),
        ),
    ]
