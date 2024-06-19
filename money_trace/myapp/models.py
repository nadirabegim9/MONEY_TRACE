from django.contrib.auth.models import User
from django.db import models


class CustomUser(User):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'last_name']

    def __str__(self):
        return self.email


