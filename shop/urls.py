from rest_framework.routers import DefaultRouter

from shop.views import ShopViewSet

router = DefaultRouter()

router.register("shop", ShopViewSet, basename="user")
urlpatterns = router.urls
