from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, TimeRecord
from django.utils import timezone
from .forms import TimeRecordForm
from django.views.generic import TemplateView, ListView
from datetime import datetime  # Correct import for using datetime.now()
import csv
from datetime import timedelta
from django.http import HttpResponse





class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        context['time_record_form'] = TimeRecordForm()
        context['pending_records'] = TimeRecord.objects.filter(time_out__isnull=True)
        context['all_records'] = TimeRecord.objects.all()  # Optimized database query
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')

        if action == 'check_in':
            self.handle_check_in(request)
        elif action == 'check_out':
            self.handle_check_out(request)
        elif action == 'add_lunch':
            self.handle_add_lunch(request)

        return redirect('home')

    def handle_check_in(self, request):
        form = TimeRecordForm(request.POST)
        if form.is_valid():
            form.save()

    def handle_check_out(self, request):
        record_id = request.POST.get('record_id')
        record = get_object_or_404(TimeRecord, id=record_id)
        record.time_out = timezone.now().time()
        record.save()

    def handle_add_lunch(self, request):
        record_id = request.POST.get('record_id')
        record = get_object_or_404(TimeRecord, id=record_id)
        record.lunch_time = timezone.timedelta(minutes=int(request.POST.get('lunch_minutes')))
        record.save()

class WeeklySummaryView(ListView):
    template_name = 'weekly_summary.html'
    context_object_name = 'time_records'
    
    def get_queryset(self):
        today = timezone.now().date()
        last_monday = today - timedelta(days=today.weekday())
        next_sunday = last_monday + timedelta(days=6)
        
        queryset = TimeRecord.objects.filter(date__range=[last_monday, next_sunday])
        for record in queryset:
            record.day_of_week = record.date.strftime('%A')
            record.working_time = record.working_hours()  # Assumes you've added this method to your model
            record.total_hours = record.working_time.total_seconds() / 3600  # Convert to hours
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        queryset = self.get_queryset()
        context['total_hours'] = sum(record.total_hours for record in queryset)
        
        return context
    
    def export_csv(request):
        today = timezone.now().date()
        last_monday = today - timedelta(days=today.weekday())
        next_sunday = last_monday + timedelta(days=6)  # Including Sunday

        queryset = TimeRecord.objects.filter(date__range=[last_monday, next_sunday])

        # Calculate total_hours for each record
        for record in queryset:
            time_in = datetime.combine(datetime.today(), record.time_in)
            time_out = datetime.combine(datetime.today(), record.time_out)
            
            # Check if lunch_time is None and default to zero if it is
            lunch_minutes = 0 if record.lunch_time is None else (record.lunch_time.seconds // 60)
            delta = time_out - time_in - timedelta(minutes=lunch_minutes)
            
            record.total_hours = delta.total_seconds() / 3600  # Convert to hours

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="weekly_summary.csv"'

        writer = csv.writer(response)
        writer.writerow(['ID', 'Nombre', 'Fecha', 'Hora de Ingreso', 'Hora de Salida', 'Tiempo de Almuerzo', 'Horas Totales'])

        for record in queryset:
            writer.writerow([record.id, record.employee.name, record.date, record.time_in, record.time_out, lunch_minutes, record.total_hours])

        return response