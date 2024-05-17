

from django import forms
from . models import Booking
from django import forms
from .models import Feedback


class DateInput(forms.DateInput):
    input_type='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'

        widgets={
            'booking_date':DateInput(),
        }

        labels={
            'cus_name':"Customer Name:",
            'cus_ph':"Customer Phone:",
            'cus_email':"Customer EmailId:",
            'name':"Event Name:",
            'booking_date':"Booking Date:",
        }


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Leave your feedback here'}),
        }
