from rest_framework.generics import CreateAPIView

from api.serializers import *


class UserCreateView(CreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = ()
