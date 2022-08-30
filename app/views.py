from django.core import serializers
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CreateSuggestionForm
from .models import Schedule, Suggestion
from . import mixins


class MonthCalendar(mixins.MonthCalendarMixin, ListView):

    model = Schedule
    template_name: str = 'app/month.html'
    ordering = 'date'
    context_object_name = "schedule_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

    def get_queryset(self):
        day = self.get_current_month()
        month = str(day).split("-")[1]
        queryset = Schedule.objects.filter(date__month=month)
        return queryset


class WeekCalendar(mixins.WeekCalendarMixin, TemplateView):
    """週間カレンダーを表示するビュー"""
    template_name = 'app/week.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class WeekWithScheduleCalendar(mixins.WeekWithScheduleMixin, TemplateView):
    """スケジュール付きの週間カレンダーを表示するビュー"""
    template_name = 'app/week_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context


class DayCalendar(mixins.DayCalendarMixin, TemplateView):
    template_name: str = 'app/day.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_day_calendar()
        context.update(calendar_context)
        return context


class DayWithScheduleCalendar(mixins.DayWithScheduleMixin, ListView):
    """1日のスケジュールを表示するビュー"""
    template_name = 'app/day_with_schedule.html'
    model = Schedule
    date_field = 'date'
    context_object_name = "schedule_list"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_day_calendar()
        context.update(calendar_context)
        context.update({'day': self.kwargs.get("day")})
        return context

    def get_queryset(self):
        day = self.get_day()
        day = str(day).split("-")[2]
        queryset = Schedule.objects.filter(date__day=day).order_by('start_time')
        print(queryset)
        return queryset


class CreateSchedule(CreateView):
    template_name: str = 'app/create.html'
    model = Schedule
    fields = (
        "title", "memo", "start_time", "end_time", "date",  "is_confirmed"
    )
    success_url = reverse_lazy("app:month_calendar")

    def get_initial(self):
        initial = super().get_initial()
        initial["date"] = self.kwargs.get("date")
        return initial

    def form_valid(self, form):
        # 重複する予定があるか検索
        new_date = form.cleaned_data.get("date")
        new_start_time = form.cleaned_data.get("start_time")
        new_end_time = form.cleaned_data.get("end_time")
        overlap_item = Schedule.objects.filter(
            Q(
                date=new_date,
                start_time__range=(new_start_time, new_end_time)
            ) | Q(
                date=new_date, start_time__gte=new_end_time
            ) | Q(
                date=new_date, end_time__lte=new_start_time
            )
        )
        if (
            self.request.POST.get('next') == "confirm"
            and len(overlap_item) > 0
        ):
            context = {"form": form}
            return render(self.request, 'app/create_alert.html', context)
        else:
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        suggestions = Suggestion.objects.all()
        suggestions_json = serializers.serialize("json", suggestions)
        context.update({
            "suggestions_json": suggestions_json,
        })
        return context


class UpdateSchedule(UpdateView):
    template_name: str = 'app/update.html'
    model = Schedule
    fields = (
        "title", "memo", "start_time", "end_time", "date", "is_confirmed"
    )
    success_url = reverse_lazy("app:month_calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"pk": self.kwargs.get("pk")})
        return context


class CreateSuggestion(CreateView):
    model = Suggestion
    form_class = CreateSuggestionForm
    template_name: str = 'app/create_suggestion.html'
    success_url = reverse_lazy('app:month_calendar')


class DeleteSchedule(DeleteView):
    template_name: str = "app/delete.html"
    model = Schedule
    success_url = reverse_lazy("app:month_calendar")
