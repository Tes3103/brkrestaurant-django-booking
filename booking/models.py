from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import User


class Table(models.Model):
    code = models.CharField(max_length=80, null=False,
                            blank=False, unique=True)
    no_of_gusts = models.IntegerField(null=False, blank=False, default=1)

    def _str_(self):
        return self.code


class Booking(models.Model):
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)
    customer_full_name = models.CharField(
        max_length=200, null=False, blank=False)
    booking_date_and_time = models.DateTimeField(null=True)

    def validate_date(reservation_date_and_time):
        if booking_date_and_time < timezone.now():
            raise ValidationError("Date should be in the future")
    booking_date_and_time = models.DateTimeField(
        null=True,
        blank=True,
        validators=[validate_date])

    customer_email = models.EmailField(max_length=100, null=False, blank=False)
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, related_name='booking_spot', blank=False)
    created_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'customer_full_name',
                           'booking_date_and_time')
        ordering = ["-created_on"]

    def __str__(self):
        return f' User {self.user} has made a booking \
                   for {self.customer_name}\
                   for {self.number_of_customers} customers\
                   for {self.reservation_date_and_time}.'
