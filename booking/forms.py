from tempus_dominus.widgets import DateTimePicker
from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('customer_full_name', 'customer_email',
                  'booking_date_and_time', 'number_of_customers')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['booking_date_and_time'].widget.attrs['class'] = 'form-control datetimepicker-input'
        self.fields['booking_date_and_time'].widget = DateTimePicker()
        self.fields['booking_date_and_time'].widget.attrs['required'] = 'required'
        self.fields['customer_email'].widget.attrs['required'] = 'required'
