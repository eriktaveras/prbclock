from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Employee, TimeRecord

class TimeRecordInline(admin.TabularInline):
    model = TimeRecord
    extra = 0
    readonly_fields = ['date', 'time_in', 'time_out', 'lunch_time']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')
    search_fields = ('name', 'position')
    list_filter = ('position',)
    inlines = [TimeRecordInline]

    fieldsets = (
        (_('Personal Information'), {'fields': ('name', 'position')}),
    )

class TimeRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', 'date', 'time_in', 'time_out', 'lunch_time')
    search_fields = ('employee__name', 'date')
    list_filter = ('date', 'employee')

    fieldsets = (
        (_('Time Record Information'), {'fields': ('employee', 'date', 'time_in', 'time_out', 'lunch_time')}),
    )

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TimeRecord, TimeRecordAdmin)
