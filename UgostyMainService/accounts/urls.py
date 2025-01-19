from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include
from .views import ProfileByNameView,PayListView,BunsListView
from . import views
#from .serializers import MyTokenObtainPairSerializer


from django.conf import settings
from django.conf.urls.static import static
from .serializers import MyTokenObtainPairSerializer

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(serializer_class=MyTokenObtainPairSerializer), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),




    path('api/user/payments/', PayListView.as_view(), name='payment-list'),

    path('api/buns/', BunsListView.as_view(), name='buns-list'),

    path('api/user/<str:username>/', ProfileByNameView.as_view(), name='user_profile'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)