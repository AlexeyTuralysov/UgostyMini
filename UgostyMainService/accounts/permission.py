from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import DonationProfile


class isNotBanned(BasePermission):
    def has_permission(self, request, view):
        try:
            banned = DonationProfile.objects.get(user=request.user)
            if banned.status_banned:
                raise PermissionDenied(detail='Вы были заблокированы')
            return True


        except DonationProfile.DoesNotExist:
            return False
            
            

