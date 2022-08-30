from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


from .forms import CreateSuggestionForm
from .models import Suggestion
from . import mixins


class MonthCalendar(mixins.MonthCalendarMixin, TemplateView):
    # model = Schedule
    template_name: str = 'app/month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        context.update(calendar_context)
        return context


class CreateSuggestionView(CreateView):
    model = Suggestion
    form_class = CreateSuggestionForm
    template_name: str = 'app/create_suggestion.html'
    success_url = reverse_lazy('app:month_calendar')

    def form_valid(self, form):
        return super().form_valid(form)
