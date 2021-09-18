from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView

from api.models import *
from api.serializers import *


class UserCreateView(CreateAPIView):
    """ Create a new user / Registration """
    serializer_class = CreateUserSerializer
    permission_classes = ()


class UserMeView(RetrieveUpdateDestroyAPIView):
    """ Show, edit and delete the current user """
    serializer_class = CreateUserSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get_object(self):
        return self.request.user


class PortfolioView(ListCreateAPIView):
    queryset = Portfolio.objects.select_related('owner').all()
    serializer_class = PortfolioSerializer


class MyPortfolioView(ListAPIView):
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return self.request.user.portfolios.select_related('owner').all()
