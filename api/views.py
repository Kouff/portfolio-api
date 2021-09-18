from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser

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


class ImageView(ListCreateAPIView):
    parser_classes = (MultiPartParser,)  # for sending image in swagger
    queryset = Image.objects.select_related('portfolio').all()
    serializer_class = ImageSerializer


class MyImageView(ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.select_related('portfolio').filter(portfolio__owner=self.request.user)
