from django.db import models
from datetime import datetime, timedelta  # Assuming you are also using timedelta


# Represents a temporary external Employee.
class Employee(models.Model):
    name = models.CharField("Name", max_length=100)
    position = models.CharField("Position", max_length=100)

    def __str__(self):
        return f"{self.name} ({self.position})"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"


# Represents a Time Record for an employee.
class TimeRecord(models.Model):
    employee = models.ForeignKey(
        Employee, 
        on_delete=models.CASCADE, 
        related_name="time_records",
        verbose_name="Employee"
    )
    date = models.DateField("Date")
    time_in = models.TimeField("Time In", null=True, blank=True)
    time_out = models.TimeField("Time Out", null=True, blank=True)
    lunch_time = models.DurationField("Lunch Time", null=True, blank=True)

    def working_hours(self):
        if self.time_in and self.time_out:
            # Create datetime objects for time_in and time_out on the same date
            dummy_date = datetime.now().date()
            dt_in = datetime.combine(dummy_date, self.time_in)
            dt_out = datetime.combine(dummy_date, self.time_out)
            
            # Check if time_out is earlier than time_in (crossing midnight)
            if dt_out < dt_in:
                # Adjust time_out to be on the next day
                dt_out += timedelta(days=1)
            
            # Calculate the time delta for working hours
            delta = dt_out - dt_in
            
            # Subtract lunch_time if it exists
            if self.lunch_time:
                delta -= self.lunch_time
            
            return delta
        else:
            return None

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

    class Meta:
        verbose_name = "Time Record"
        verbose_name_plural = "Time Records"
        unique_together = ("employee", "date")
