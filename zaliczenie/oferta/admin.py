from django.contrib import admin


# Register your models here.

from .models import Sell


class AdminSell(admin.ModelAdmin):
    list_display = ('name','price')
admin.site.register(Sell, AdminSell)