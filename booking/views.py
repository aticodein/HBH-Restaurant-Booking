from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import bookingItem
from .forms import bookingItemForm

# Create your views here.


def display_bookings(request):
    BookingItems = bookingItem.objects.all().order_by('-date', 'time')

    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You did not enter search')
                return redirect(reverse('display_bookings'))

            queries = (Q(name__icontains=query) | Q(comment__icontains=query)
                       | Q(roomNum__icontains=query))
            BookingItems = BookingItems.filter(queries)

        if 'date_search' in request.GET:
            query = request.GET['date_search']
            if not query:
                messages.error(request, 'You did not enter search')
                return redirect(reverse('display_bookings'))

            queries = Q(date__icontains=query)
            BookingItems = BookingItems.filter(queries)

    context = {
        'BookingItems': BookingItems,
        'serch_term': query,
        'bookingItem.adultNum': bookingItem.adultNum,
    }

    print(f"Ez van a contextben, ez megy az oldalra: {context} *********")
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
    messages.error(request, 'You are editing this booking')
    context = {
        'form': form
    }
    return render(request, 'bookings/edit_bookings.html', context)


def delete_booking(request, bookingItem_id):
    item = get_object_or_404(bookingItem, id=bookingItem_id)
    item.delete()

    return redirect('display_bookings')
