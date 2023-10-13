from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_service_provider = models.BooleanField(default=False)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.username
