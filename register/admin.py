from django.contrib import admin
from .models import MicroApp,Transaction,BookingItem

# Register your models here.
admin.site.register(MicroApp)
admin.site.register(Transaction)
admin.site.register(BookingItem)