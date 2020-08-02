from .models import bookingItem


class OrderFilter():
    class Meta:
        model = bookingItem
        fields = '__all__'
