from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Booking, Table


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = ('user', 'customer_full_name',
                    'booking_date_and_time',
                    'customer_email',
                    'number_of_customers', 'table')
    search_fields = ('customer_name',
                     'booking_date_and_time',
                     'customer_email')
    list_filter = ('customer_full_name',
                   'booking_date_and_time',
                   'customer_email')
