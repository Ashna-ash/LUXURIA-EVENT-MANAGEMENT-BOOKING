

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Events1(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=500)
    details = models.TextField(default='')  # Provide a default value here
    cost = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name = models.CharField(max_length=55)
    cus_ph = models.CharField(max_length=12)
    cus_email = models.EmailField(max_length=50, default='')
    event_name = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def remove_booking(self):
        # Custom method to remove a booking
        self.delete()  # This will delete the booking instance from the database

class EventDetail(models.Model):
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    details = models.CharField(max_length=1000)
    def __str__(self):
        return f"Details for {self.event.name}"


class Feedback(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='feedback_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Feedback {self.pk}"