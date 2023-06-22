from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

class User(AbstractUser):
    watchlist = models.ManyToManyField(
        'auctions', blank=True, related_name="watchlist")
    

class auctions(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    bid = models.IntegerField(validators=[MinValueValidator(1)])
    image = models.URLField(max_length=2048, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="auctions")
    active = models.BooleanField(default=True)
    class category(models.TextChoices):
        FASHION = 'Fashion'
        TOYS = 'Toys'
        ELECTRONICS = 'Electronics'
        HOME = 'Home'
        OTHER = 'Other'
    category = models.CharField(
        max_length=64, choices=category.choices, default=category.OTHER)
    


class bid(models.Model):
    bid = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bids")
    auction = models.ForeignKey(
        'auctions', on_delete=models.CASCADE, related_name="bids")


class comments(models.Model):
    comment = models.CharField(max_length=64)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    auction = models.ForeignKey(
        'auctions', on_delete=models.CASCADE, related_name="comments")
    def __str__(self):
        return f"{self.user} : {self.comment}"
