from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.IntegerField(blank=True, null=True)
    dob = models.DateField(db_column='DoB', blank=True, null=True)

    class Meta:
        db_table = 'user'
