from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reference = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    confirmed = models.BooleanField(default=True)

    def __str__(self):
        return self.reference
