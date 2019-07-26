from django.db import models
from utils.common.cipher import AESCipher

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = "users"

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    email = models.CharField(max_length = 128, unique = True)
    password = models.CharField(max_length = 255)
    is_email_authenticated = models.BooleanField(default=False)


# https://inma.tistory.com/116?category=984128