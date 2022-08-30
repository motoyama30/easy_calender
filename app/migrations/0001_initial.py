# Generated by Django 4.1 on 2022-08-30 10:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="タイトル")),
                ("memo", models.TextField(blank=True, verbose_name="メモ")),
                (
                    "start_time",
                    models.TimeField(default=datetime.time(10, 0), verbose_name="開始時刻"),
                ),
                (
                    "end_time",
                    models.TimeField(default=datetime.time(10, 0), verbose_name="終了時刻"),
                ),
                (
                    "is_confirmed",
                    models.BooleanField(default=True, verbose_name="確定済み"),
                ),
            ],
            options={"verbose_name": "候補", "verbose_name_plural": "候補一覧",},
        ),
        migrations.CreateModel(
            name="Schedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("memo", models.TextField(blank=True, null=True, verbose_name="メモ")),
                (
                    "start_time",
                    models.TimeField(default=datetime.time(10, 0), verbose_name="開始時刻"),
                ),
                (
                    "end_time",
                    models.TimeField(default=datetime.time(10, 0), verbose_name="終了時刻"),
                ),
                ("date", models.DateField(verbose_name="日付")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="作成日"),
                ),
                (
                    "is_confirmed",
                    models.BooleanField(default=True, verbose_name="確定したか"),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="app.suggestion",
                        verbose_name="タイトル",
                    ),
                ),
            ],
            options={"verbose_name": "予定", "verbose_name_plural": "予定一覧",},
        ),
    ]
