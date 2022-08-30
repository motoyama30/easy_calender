# Generated by Django 4.1 on 2022-08-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_suggestion_is_confirmed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='suggestion',
            name='is_confirmed',
            field=models.BooleanField(default=True, verbose_name='確定済み'),
        ),
    ]
