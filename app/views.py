from django.views.generic import TemplateView

# from app.models import Schedule
from . import mixins


class MonthCalendar(mixins.MonthCalendarMixin, TemplateView):
    # model = Schedule
    template_name: str = 'app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context
