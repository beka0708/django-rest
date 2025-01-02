from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    is_check = models.BooleanField(default=False)

    def __str__(self):
        return self.last_name
