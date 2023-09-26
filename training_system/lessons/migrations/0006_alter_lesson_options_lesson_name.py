# Generated by Django 4.2.5 on 2023-09-26 01:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_alter_lesson_date_alter_training_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Урок', 'verbose_name_plural': 'Уроки'},
        ),
        migrations.AddField(
            model_name='lesson',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=123),
            preserve_default=False,
        ),
    ]
