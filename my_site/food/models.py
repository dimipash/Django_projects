from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Item(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://img.freepik.com/free-vector/green-restaurant-menu-background_23-2147490040.jpg?w=740&t=st=1692250749~exp=1692251349~hmac=2b7f6638a23793d5969690a5ed403d8b47ab0d45371df6c00cc2a43b50e28b6d")

    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
