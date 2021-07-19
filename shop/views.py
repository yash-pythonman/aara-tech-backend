from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from shop.models import Shop
from shop.serializers import LatLongSerializer, ShopSerializer
from shop.services import CreateShopService
from shop.utils import get_distance


class ShopViewSet(ViewSet):
    """
    ViewSet created to perform CRUD operation on shop model.
    """

    @staticmethod
    def create(request):
        """
        Method create to handle http post request to create shop details.
        """
        payload = ShopSerializer(data=request.data)
        if payload.is_valid(raise_exception=True):
            return CreateShopService.execute(payload.validated_data)

    @staticmethod
    def list(request):
        """
        Method create to handle http get request to provide nearest shop list.
        """
        params = LatLongSerializer(data=request.GET)
        if params.is_valid(raise_exception=True):
            response = [
                {
                    "name": shop.name,
                    "id": shop.id,
                    "distance": get_distance(
                        shop,
                        params.validated_data["lat"],
                        params.validated_data["long"],
                    ),
                }
                for shop in Shop.objects.filter()
            ]
            response.sort(key=lambda item: item["distance"])
            return Response(response)

    @staticmethod
    def retrieve(_, pk):
        """
        Method created to handle http get request to provide shop details.
        """
        try:
            return Response(ShopSerializer(Shop.objects.get(id=pk)).data)
        except Shop.DoesNotExist:
            return Response({"Error": f"Invalid shop id {pk}."})
