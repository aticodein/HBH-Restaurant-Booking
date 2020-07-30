from django import forms
from .models import bookingItem


class bookingItemForm(forms.ModelForm):
    class Meta:
        model = bookingItem
        fields = ['name', 'roomNum', 'date', 'time', 'adultNum', 'childNum',
                  'highChair', 'comment', 'email']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'date',
                                    'placeholder': 'Only this format! 2020-07-26'},
                                    format='%Y-%m-%d'),
            'time': forms.TimeInput(attrs={'class': 'time',
                                    'placeholder': 'Only this format! 18:30'})
        }
