import datetime
from django.db import models
from django.utils import timezone


class Suggestion(models.Model):
    """候補"""
    title = models.CharField('タイトル', max_length=50)
    memo = models.TextField('メモ', blank=True)
    start_time = models.TimeField('開始時刻', default=datetime.time(10, 0, 0))
    end_time = models.TimeField('終了時刻', default=datetime.time(10, 0, 0))

    class Meta:
        verbose_name = "候補"
        verbose_name_plural = "候補一覧"

    def __str__(self) -> str:
        return self.title


class Schedule(models.Model):
    """予定"""
    title = models.ForeignKey(
        Suggestion, verbose_name='タイトル', on_delete=models.PROTECT
    )
    memo = models.TextField('メモ', null=True, blank=True)
    start_time = models.TimeField('開始時刻', default=datetime.time(10, 0, 0))
    end_time = models.TimeField('終了時刻', default=datetime.time(10, 0, 0))
    date = models.DateField('日付')
    created_at = models.DateTimeField('作成日', default=timezone.now)
    is_confirmed = models.BooleanField('確定したか', default=True)

    def __str__(self) -> str:
        return f'{self.date}; {self.title}'

    class Meta:
        verbose_name = "予定"
        verbose_name_plural = "予定一覧"
