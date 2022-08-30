from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from app.models import Schedule

# from app.models import Schedule
from . import mixins


class MonthCalendar(mixins.MonthCalendarMixin, TemplateView):
    model = Schedule
    template_name: str = 'app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context

class CreateSchedule(CreateView):
    template_name: str = 'app/create.html'
    model = Schedule
    fields = ("title", "memo", "start_time", "end_time", "date", "is_confirmed")
    success_url = reverse_lazy("app:month_calendar")

class UpdateSchedule(UpdateView):
    template_name: str = 'app/update.html'
    model = Schedule
    fields = ("title", "memo", "start_time", "end_time", "date", "is_confirmed")
    success_url = reverse_lazy("app:month_calendar")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"pk":self.kwargs.get("pk")})
        return context

class DeleteSchedule(DeleteView):
    template_name: str = "app/delete.html"
    model = Schedule
    success_url = reverse_lazy("app:month_calendar")



