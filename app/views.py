from django.views.generic import ListView
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


class UpdateSchedule(UpdateView):
    template_name: str = 'app/update.html'
    model = Schedule
    fields = (
        "title", "memo", "start_time", "end_time", "date", "is_confirmed"
    )
    # success_url = reverse_lazy("app:month_calendar")


class CreateSuggestion(CreateView):
    model = Suggestion
    form_class = CreateSuggestionForm
    template_name: str = 'app/create_suggestion.html'
    success_url = reverse_lazy('app:month_calendar')
