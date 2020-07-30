from django.db import models

# Create your models here.


class bookingItem(models.Model):
    name = models.CharField(max_length=49, null=False, blank=False)
    time = models.TimeField(auto_now=False, auto_now_add=False,
                            null=False, blank=False)
    adultNum = models.DecimalField(max_digits=2, decimal_places=0,
                                   null=False, blank=False)
    date = models.DateField(auto_now=False, auto_now_add=False,
                            null=False, blank=False)
    childNum = models.DecimalField(max_digits=2, decimal_places=0,
                                   null=False, blank=False)
    highChair = models.DecimalField(max_digits=1, decimal_places=0,
                                    null=False, blank=False)
    roomNum = models.DecimalField(max_digits=3, decimal_places=0,
                                  null=False, blank=False)
    comment = models.CharField(max_length=199, null=False, blank=False)
    email = models. EmailField(max_length=254, null=False, blank=True)

    def __str__(self):
        return self.name
