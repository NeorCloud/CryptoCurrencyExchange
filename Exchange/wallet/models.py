from django.db import models
from django.contrib.auth.models import User


class Token(models.Model):
    name = models.TextField(blank=False)
    symbol = models.TextField(max_length=10, blank=False)
    actual_price = models.FloatField(blank=False)
    image = models.ImageField(default='bitcoin_icon.jpg', upload_to='token_logo')

    def __str__(self):
        return f"{self.name}"


class Wallet(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0.0, blank=False)
    address = models.TextField(blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Wallet of {self.owner} - {self.token}"


class History(models.Model):
    token = models.ForeignKey(Token, on_delete=models.CASCADE)
    price = models.FloatField()
    date_time = models.DateTimeField(blank=False)

    def __str__(self):
        return f"History of {self.token} - {self.date_time}"