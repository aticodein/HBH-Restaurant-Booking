"""HBH_restaurant_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from booking import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('add_booking', views.add_booking, name='add_booking'),
    path('display_bookings/', views.display_bookings, name='display_bookings'),
    path('edit_booking/<bookingItem_id>', views.edit_booking,
         name='edit_booking'),
    path('delete_booking/<bookingItem_id>', views.delete_booking,
         name='delete_booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
