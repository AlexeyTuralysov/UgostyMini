from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DonationProfile,Payment, Buns,DonationBunQuantity

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import authenticate, login, logout


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['is_admin_user'] = user.is_superuser

        # Add the nickname from DonationProfile
        try:
            donation_profile = DonationProfile.objects.get(user=user)
            token['nickname'] = donation_profile.nickname

        except DonationProfile.DoesNotExist:
            token['nickname'] = None

        return token


class UserSerialuzerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username')



class BunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buns
        fields = ['id', 'name', 'img_buns', 'price', 'created_at','color_treats']

class DonationBunQuantitySerializer(serializers.ModelSerializer):
    bun = BunsSerializer()

    class Meta:
        model = DonationBunQuantity
        fields = ['bun', 'quantity']

class DonationProfileSerializer(serializers.ModelSerializer):
    buns = serializers.SerializerMethodField()

    class Meta:
        model = DonationProfile
        fields = ['id', 'user', 'nickname', 'description', 'image', 'buns','status_banned']

    def get_buns(self, obj):
        donation_buns = DonationBunQuantity.objects.filter(donation_profile=obj)
        return DonationBunQuantitySerializer(donation_buns, many=True).data




class OutBunsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buns
        fields = '__all__'


class PayoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

    def create(self, validData):
        user = User.objects.create(
            username=validData['username'],
            email=validData['email'],

        )
        user.set_password(validData['password'])
        user.save()
        return user

