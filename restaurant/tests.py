
from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIClient

from .models import Booking, MenuItem


class RestaurantApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item = MenuItem.objects.create(
            title="Greek Salad",
            price="12.50",
            inventory=8,
            description="Fresh salad",
        )
        self.user = get_user_model().objects.create_user(
            username="sam", password="StrongPass123!"
        )

    def test_home_page_returns_html(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Little Lemon")

    def test_menu_list(self):
        response = self.client.get("/api/menu/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["title"], "Greek Salad")

    def test_menu_item_detail(self):
        response = self.client.get(f"/api/menu/{self.menu_item.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["price"], "12.50")

    def test_create_menu_item(self):
        response = self.client.post(
            "/api/menu/",
            {
                "title": "Pasta",
                "price": "15.00",
                "inventory": 5,
                "description": "House pasta",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(MenuItem.objects.filter(title="Pasta").exists())

    def test_update_menu_item(self):
        response = self.client.patch(
            f"/api/menu/{self.menu_item.id}/",
            {"price": "13.00"},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.menu_item.refresh_from_db()
        self.assertEqual(str(self.menu_item.price), "13.00")

    def test_delete_menu_item(self):
        response = self.client.delete(
            f"/api/menu/{self.menu_item.id}/"
        )
        self.assertEqual(response.status_code, 204)
        self.assertFalse(
            MenuItem.objects.filter(pk=self.menu_item.pk).exists()
        )

    def test_create_booking(self):
        payload = {
            "first_name": "Taylor",
            "reservation_date": (
                timezone.localdate() + timedelta(days=2)
            ).isoformat(),
            "reservation_slot": 14,
        }
        response = self.client.post(
            "/api/bookings/", payload, format="json"
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.first().first_name, "Taylor")

    def test_reject_past_booking(self):
        payload = {
            "first_name": "Taylor",
            "reservation_date": (
                timezone.localdate() - timedelta(days=1)
            ).isoformat(),
            "reservation_slot": 14,
        }
        response = self.client.post(
            "/api/bookings/", payload, format="json"
        )
        self.assertEqual(response.status_code, 400)

    def test_booking_list(self):
        Booking.objects.create(
            first_name="Taylor",
            reservation_date=timezone.localdate() + timedelta(days=1),
            reservation_slot=14,
        )
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]["first_name"], "Taylor")

    def test_registration(self):
        response = self.client.post(
            "/api/registration/",
            {
                "username": "newuser",
                "email": "new@example.com",
                "password": "AnotherStrong123!",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(
            get_user_model().objects.filter(username="newuser").exists()
        )

    def test_token_login(self):
        response = self.client.post(
            "/api/token/",
            {
                "username": "sam",
                "password": "StrongPass123!",
            },
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("token", response.data)
