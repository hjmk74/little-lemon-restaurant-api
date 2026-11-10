
from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Booking, MenuItem
from .serializers import (
    BookingSerializer,
    MenuItemSerializer,
    RegistrationSerializer,
)


def home(request):
    menu_items = MenuItem.objects.all()[:6]
    return render(request, "restaurant/index.html", {"menu_items": menu_items})


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [permissions.AllowAny]


class ObtainTokenView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        from django.contrib.auth import authenticate

        username = request.data.get("username", "")
        password = request.data.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {"detail": "Invalid username or password."},
                status=400,
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
