from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegistrationSerializer,PayoutSerializer,DonationProfileSerializer, OutBunsSerializer,BunsSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import DonationProfile, Payment,Buns

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.exceptions import APIException

from rest_framework.views import APIView

from .permission import isNotBanned
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import views
from rest_framework import permissions
from rest_framework import serializers
from django.contrib.auth import authenticate, login, logout
import json
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST

from django_filters import rest_framework as filters
from django_filters import DateFilter
class ProfileByNameView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = DonationProfileSerializer

    def get_queryset(self):
        return DonationProfile.objects.all()

    def get(self, request, username, *args, **kwargs):
        profile = self.get_object()
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    def get_object(self):
        username = self.kwargs.get('username')
        try:
            return DonationProfile.objects.get(user__username=username)
        except DonationProfile.DoesNotExist:
            raise APIException("Profile not found")


class BunsListView(generics.ListAPIView):
    permission_classes = (AllowAny,)

    serializer_class = OutBunsSerializer

    def get_queryset(self):
        return Buns.objects.all()



class ModelFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Payment
        fields = ['created_at']

class PayListView(generics.ListAPIView):
    serializer_class = PayoutSerializer
    permission_classes = [IsAuthenticated,isNotBanned]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ModelFilter

    def get_queryset(self):
        user = self.request.user

        return Payment.objects.filter(donation_profile__user=user)

