from django.db import models

# Create your models here.
from screens.models import ScreenSeat
from ssafbox import settings


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    seats = models.ForeignKey(ScreenSeat, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()
    uuid = models.CharField(max_length=100)
    tid = models.CharField(max_length=100, null=True, default=None)
    is_paid = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['uuid']),
        ]
