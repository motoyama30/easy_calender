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
    path('week/', views.WeekCalendar.as_view(), name='week'),
    path(
        'week/<int:year>/<int:month>/<int:day>/',
        views.WeekCalendar.as_view(),
        name='week'
    ),
    path(
        'week_with_schedule/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'),
    path(
        'week_with_schedule/<int:year>/<int:month>/<int:day>/',
        views.WeekWithScheduleCalendar.as_view(),
        name='week_with_schedule'
    ),
    path('sample_day/', views.DayCalendar.as_view(), name='day'),
    path(
        'sample_day/<int:year>/<int:month>/<int:day>/',
        views.DayCalendar.as_view(),
        name='day'),
    path('sample_day_schedule/', views.DayWithScheduleCalendar.as_view(), name='day_with_schedule'),
    path(
        'sample_day_schedule/<int:year>/<int:month>/<int:day>/',
        views.DayWithScheduleCalendar.as_view(),
        name='day_with_schedule'
    ),

    path(
        "create/",
        views.CreateSchedule.as_view(),
        name="create"
    ),

    path(
        "update/<int:pk>",
        views.UpdateSchedule.as_view(),
        name="update",
    ),
    path(
        "delete/<int:pk>",
        views.DeleteSchedule.as_view(),
        name="delete"
    )


]
