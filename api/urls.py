from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import *

urlpatterns = [
    path('registration/', UserCreateView.as_view()),
    path('users/me/', UserMeView.as_view()),
    path('portfolios/', PortfolioView.as_view()),
    path('portfolios/my/', MyPortfolioView.as_view()),
    path('portfolios/<int:pk>/', PortfolioDetailView.as_view()),
    path('images/', ImageView.as_view()),
    path('images/my/', MyImageView.as_view()),
    path('images/<int:pk>/', ImageDetailView.as_view()),
    path('comments/', CommentCreateView.as_view()),
    path('comments/<int:pk>/', CommentView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
]
