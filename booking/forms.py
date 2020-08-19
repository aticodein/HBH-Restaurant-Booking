from django import forms
from .models import bookingItem


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'date.time'


class bookingItemForm(forms.ModelForm):
    class Meta:
        model = bookingItem
        bookedData = bookingItem.objects.filter().last()
        boo = bookedData.time

        boo = str(boo)

        boo = boo.split(':')

        boo = (''.join(boo))

        boo = int(boo)

        print(f"*** bookedData.time is an int: {boo} ***")

        fields = ['name', 'roomNum', 'date', 'time', 'adultNum', 'childNum',
                  'highChair', 'comment', 'email']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker',
                                           'type': 'date',
                                    'placeholder': 'Use format! 2020-07-26'},
                                    format='%Y-%m-%d')
        }
