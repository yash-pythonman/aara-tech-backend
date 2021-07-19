from rest_framework import status
from rest_framework.response import Response
from service_objects.services import Service

from shop.models import Shop


class CreateShopService(Service):
    def process(self):
        return Response(
            {"shop_id": Shop.objects.create(**self.data).id},
            status=status.HTTP_201_CREATED,
        )
