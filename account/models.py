from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, phone_number, password=None, city=None):
        if not phone_number:
            raise ValueError('Raqam Xato')
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            phone_number=phone_number,
            city=city,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, first_name, last_name, phone_number, city, password):
        user = self.create_user(
            first_name = first_name,
            last_name = last_name,
            password = password,
            phone_number=phone_number,
            city=city,) 
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    city = models.CharField(max_length=50, default=None)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'city']

    objects = MyAccountManager()
    
    def __str__(self) -> str:
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True