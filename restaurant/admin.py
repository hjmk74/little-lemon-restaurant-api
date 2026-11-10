from django.contrib import admin
from .models import MenuItem, Booking


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "inventory")
    search_fields = ("title",)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "reservation_date",
        "reservation_slot",
    )
    list_filter = ("reservation_date",)
    search_fields = ("first_name",)