from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
    )
    inventory = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Booking(models.Model):
    first_name = models.CharField(max_length=100)
    reservation_date = models.DateField()
    reservation_slot = models.PositiveSmallIntegerField(default=10)

    class Meta:
        ordering = ["reservation_date", "reservation_slot"]

    def __str__(self):
        return f"{self.first_name} - {self.reservation_date} ({self.reservation_slot})"
