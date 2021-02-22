from django.contrib import admin
from .models import MicroApp,Transaction

# Register your models here.
admin.site.register(MicroApp)
admin.site.register(Transaction)