from django.shortcuts import render, redirect, get_object_or_404
from .models import bookingItem
from .forms import bookingItemForm


# Create your views here.


def display_bookings(request):
    BookingItems = bookingItem.objects.all()
    context = {
        'BookingItems': BookingItems
    }
    return render(request, 'bookings/display_bookings.html', context)


def add_booking(request):
    if request.method == 'POST':
        form = bookingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_bookings')

    form = bookingItemForm()
    context = {
        'form': form
    }
    return render(request, 'bookings/add_bookings.html', context)


def edit_booking(request, bookingItem_id):
    item = get_object_or_404(bookingItem, id=bookingItem_id)
    if request.method == 'POST':
        form = bookingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_bookings')
    form = bookingItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'bookings/edit_bookings.html', context)


def delete_booking(request, bookingItem_id):
    item = get_object_or_404(bookingItem, id=bookingItem_id)
    item.delete()

    return redirect('display_bookings')

