from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.contrib.auth.models import User

# Create your models here.

class Users(AbstractUser):
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    number = models.CharField(max_length=20)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    number = models.IntegerField(default=0, null=True)
    block = models.BooleanField(default=False)
    gender = models.CharField(max_length=10)
    position = models.TextField()

    def __str__(self):
        return self.username

class Items(models.Model):
    item_name = models.CharField(max_length=100)
    out_number = models.CharField(max_length=100)
    catigory = models.CharField(max_length=100, null=True)
    price = models.FloatField(default=0.0)
    old_price = models.FloatField(default=0.0)
    color = models.CharField(max_length=100, null=True)
    picture = models.ImageField(upload_to='picture')
    total_quantity = models.PositiveIntegerField(default=0)
    available = models.BooleanField(default=True)
    add_to_store = models.BooleanField(default=True)

    def __str__(self):
        return self.item_name
    
class Messages(models.Model):
    sent_date = models.DateTimeField(auto_now=True)
    sender_name = models.CharField(max_length=100)
    sender_number = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.sender_name

class SellReports(models.Model):
    item_name = models.CharField(max_length=150)
    item_price = models.FloatField(default=0.0)
    item_quantity = models.PositiveIntegerField(default=0)
    sell_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sell_name.out_number


class Carts(models.Model):
    # buyer_name = models.CharField(max_length=100)
    buyer_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    but_date = models.DateTimeField(auto_now=True)
    price = models.FloatField(default=0.0)
    out_number = models.CharField(max_length=100)
    catigory = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    total_price = models.FloatField(default=0.0)
    item_name = models.CharField(max_length=150)

    def __str__(self):
        return self.buyer_name.username

class Histories(models.Model):
    # buyer_name = models.CharField(max_length=100)
    buyer_name = models.ForeignKey(Users, on_delete=models.CASCADE)
    but_date = models.DateTimeField(auto_now=True)
    out_number = models.CharField(max_length=100)
    catigory = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField(default=0.0)
    Item_name = models.CharField(max_length=150)

    def __str__(self):
        return self.buyer_name.username