from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
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


class DayWithScheduleCalendar(mixins.DayWithScheduleMixin, TemplateView):
    """スケジュール付きの週間カレンダーを表示するビュー"""
    template_name = 'app/day_with_schedule.html'
    model = Schedule
    date_field = 'date'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_day_calendar()
        context.update(calendar_context)
        return context


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


# class CreateAlert(TemplateView):
    # template_name: str = "app/create_alert.html"


class UpdateSchedule(UpdateView):
    template_name: str = 'app/update.html'
    model = Schedule
    fields = (
        "title", "memo", "start_time", "end_time", "date", "is_confirmed"
    )
    success_url = reverse_lazy("app:month_calendar")


class CreateSuggestion(CreateView):
    model = Suggestion
    form_class = CreateSuggestionForm
    template_name: str = 'app/create_suggestion.html'
    success_url = reverse_lazy('app:month_calendar')
