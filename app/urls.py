from django.urls import path
from . import views


app_name = 'app'

urlpatterns = [
    path('', views.MonthCalendar.as_view(), name='month_calendar'),
    path(
        'month/<int:year>/<int:month>/',
        views.MonthCalendar.as_view(),
        name='month_calendar_month',
    ),
    path(
        'create_suggestion/',
        views.CreateSuggestionView.as_view(),
        name='create_suggestion'
    ),
]
