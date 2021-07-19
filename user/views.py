from rest_framework.views import APIView

from user.serializers import UserSerializer
from user.services import RegistrationService


class RegistrationView(APIView):
    """
    View created to register new user.
    """

    @staticmethod
    def post(request):
        """
        Function created to handle http post request and create a new user.
        """
        payload = UserSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return RegistrationService.execute(payload.validated_data)
