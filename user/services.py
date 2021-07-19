from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service


class RegistrationService(Service):
    """
    Service created to insert user details into db.
    """

    def process(self):
        User.objects.create_user(**self.data, is_staff=True)
        return Response(
            {"Message": "User created successfully."}, status=status.HTTP_201_CREATED
        )
