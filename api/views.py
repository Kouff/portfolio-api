from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated

from api.models import *
from api.permissions import IsOwnerOrReadOnly, IsOwnerForImageOrReadOnly
from api.serializers import *


class UserCreateView(CreateAPIView):
    """
    get: Registration / Create a new user.
    """
    serializer_class = CreateUserSerializer
    permission_classes = ()


class UserMeView(RetrieveUpdateDestroyAPIView):
    """
    get: Show the current user.
    patch: Edit the current user.
    delete: Delete the current user.
    """
    serializer_class = CreateUserSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get_object(self):
        return self.request.user


class PortfolioView(ListCreateAPIView):
    """
    get: Show all the portfolios.
    post: Create a new portfolio.
    """
    queryset = Portfolio.objects.select_related('owner').all()
    serializer_class = PortfolioSerializer


class MyPortfolioView(ListAPIView):
    """
    get: Show all portfolios of the current user.
    """
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return self.request.user.portfolios.select_related('owner').all()


class PortfolioDetailView(RetrieveUpdateDestroyAPIView):
    """
    get: Show a portfolio with images.
    patch: Edit a portfolio (for the portfolio owner only).
    delete: Delete a portfolio (for the portfolio owner only).
    """
    queryset = Portfolio.objects.select_related('owner').prefetch_related('images').all()
    serializer_class = PortfolioDetailSerializer
    http_method_names = ['get', 'patch', 'delete']
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class ImageView(ListCreateAPIView):
    """
    get: Show all the images.
    post: Create a new image.
    """
    parser_classes = (MultiPartParser,)  # for sending image in swagger
    queryset = Image.objects.select_related('portfolio').all()
    serializer_class = ImageSerializer


class MyImageView(ListAPIView):
    """
    get: Show all images of the current user.
    """
    serializer_class = ImageSerializer

    def get_queryset(self):
        return Image.objects.select_related('portfolio').filter(portfolio__owner=self.request.user)


class ImageDetailView(RetrieveUpdateDestroyAPIView):
    """
    get: Show a image with comments.
    patch: Edit a image (for the image owner only).
    delete: Delete a image (for the image owner only).
    """
    queryset = Image.objects.select_related('portfolio').prefetch_related('comments__author').all()
    serializer_class = ImageDetailSerializer
    http_method_names = ['get', 'patch', 'delete']
    permission_classes = (IsAuthenticated, IsOwnerForImageOrReadOnly)
