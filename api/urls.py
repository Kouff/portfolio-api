from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import *

urlpatterns = [
    path('registration/', UserCreateView.as_view()),
    path('users/me/', UserMeView.as_view()),
    path('portfolios/', PortfolioView.as_view()),
    path('portfolios/my/', MyPortfolioView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
