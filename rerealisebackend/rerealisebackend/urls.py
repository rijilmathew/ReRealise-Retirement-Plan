from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import ( TokenRefreshView,TokenVerifyView)
from authentification.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/verify/', TokenVerifyView.as_view()),
    path('api/authentification',include('authentification.urls')),

]
