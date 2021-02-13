from django.contrib import admin

# Register your models here.
from amsmain.models import InsertImage, Register


class InsertImageadmin(admin.ModelAdmin):
    list_display = ('imagename', 'image', 'category')


admin.site.register(InsertImage, InsertImageadmin)


class Bookings(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date', 'event', 'description')


admin.site.register(Register, Bookings)
