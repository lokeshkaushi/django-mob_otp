import email
from typing_extensions import Self
from unicodedata import name
import uuid
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True,)
    mobile=models.CharField(max_length=20,unique=True,default='+91')
    otp =models.CharField(max_length=8,null=True,blank=True)
    uid =models.UUIDField(default=uuid.uuid4)
    forget_password_token= models.CharField(max_length=100 ,null=True,blank=True)
