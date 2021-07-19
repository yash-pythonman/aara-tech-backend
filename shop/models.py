from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    """
    Model created to store shop details.
    """

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    lat = models.FloatField()
    long = models.FloatField()

    class Meta:
        db_table = "shop"


class Review(models.Model):
    """
    Model created to store review details.
    """

    review = models.CharField(max_length=255)
    user = models.ForeignKey(
        User, on_delete=models.DO_NOTHING, related_name="review_of_users"
    )
    shop = models.ForeignKey(
        Shop, on_delete=models.DO_NOTHING, related_name="review_for_shop"
    )

    class Meta:
        db_table = "review"
