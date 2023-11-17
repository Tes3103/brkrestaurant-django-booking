from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Booking
from .forms import BookingForm


def handler404(request, *args, **argv):
    form = BookingForm()
    context = {
        'form': form
    }
    response = render(request, 'booking/not_found.html', context)
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    bookings = Booking.objects.all()
    context = {
        'bookings': bookings
    }
    response = render(request, 'booking/duplicate_booking.html', context)
    response.status_code = 500
    return response


def view_home(request):
    return render(request, 'booking/index.html')


def contact(request):
    return render(request, 'booking/contact.html')


@login_required
def add_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Booking successful.')
            return redirect('view_booking')
        else:
            messages.error(request, 'Booking date must be in the future.')
    form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking/add_booking.html', context)


@login_required
def view_booking(request):
    """
    Function enables user to view a booking after
    it has been made and added to the database.
    """
    bookings = Booking.objects.filter(user__in=[request.user])
    context = {
        'bookings': bookings
    }
    return render(request, 'booking/view_booking.html', context)


@login_required
def edit_booking(request, booking_id):
    book = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=book)
        if form.is_valid():
            booking = form.save()
            booking.user = request.user
            booking.save()
            messages.success(request, 'Your booking has been updated.')
        return redirect('view_booking')
    form = BookingForm(instance=book)
    context = {
        'form': form
    }
    return render(request, 'booking/edit_booking.html', context)


@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if booking.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('view_booking')

    form = BookingForm(instance=booking)
    context = {
        'form': form
    }
    return render(request, 'booking/delete_booking.html', context)
