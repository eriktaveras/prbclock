# employee_app/urls.py

from django.urls import path
from .views import HomePageView, WeeklySummaryView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('weekly_summary/', WeeklySummaryView.as_view(), name='weekly_summary'),
    path('weekly_summary/export_csv/', WeeklySummaryView.export_csv, name='export_csv'),  # Agrega esta línea


]
