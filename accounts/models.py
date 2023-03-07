from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, phone, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        # """
        # if not email:
        #     raise ValueError('Users must have an email address')

        user = self.model(
            # email=self.normalize_email(email),
            phone=phone,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            # email,
            password=password,
            phone=phone,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


    
class UserModel(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        blank=True,
        null=True,
    )
    name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تلفن',unique=True)
    date_join = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ عضویت')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    class Meta:
        verbose_name = 'مشتری'
        verbose_name_plural = 'مشتری ها'

    def __str__(self):
        return self.name+self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    


class Address(models.Model):
    user = models.ForeignKey(to=UserModel,on_delete=models.CASCADE,related_name='address')
    address = models.CharField(max_length=300, verbose_name='آدرس',)
    
    def __str__(self):
        return self.address
    
    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'