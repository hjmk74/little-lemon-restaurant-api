from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, BookingViewSet, RegisterView, ObtainTokenView

router = DefaultRouter()
router.register("menu", MenuItemViewSet, basename="menu")
router.register("bookings", BookingViewSet, basename="bookings")

urlpatterns = [
    path("", include(router.urls)),
    path("registration/", RegisterView.as_view(), name="registration"),
    path("token/", ObtainTokenView.as_view(), name="token"),
]
