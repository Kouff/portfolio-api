from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView

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
