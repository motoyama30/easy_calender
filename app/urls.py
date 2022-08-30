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
        "create/<str:date>",
        views.CreateSchedule.as_view(),
        name="create"
    ),
    path(
        "update/<int:pk>",
        views.UpdateSchedule.as_view(),
        name="update",
    ),
    path(
        'create_suggestion/',
        views.CreateSuggestion.as_view(),
        name='create_suggestion'
    ),
]
