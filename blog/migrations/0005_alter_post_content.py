# Generated by Django 4.2.7 on 2024-08-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default='Здесь будет контент ...', verbose_name='Текст статьи'),
        ),
    ]