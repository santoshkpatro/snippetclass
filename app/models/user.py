from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Users must have first name')

        user = self.model(email=self.normalize_email(email), first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_instructor(self, email, first_name, password=None, **extra_fields):
        user = self.create_user(email, first_name, password, **extra_fields)
        user.is_instructor = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None, **extra_fields):
        user = self.create_user(email, first_name, password, **extra_fields)
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    avatar = models.URLField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    password_reset_required = models.BooleanField(default=False)
    password_reset_token = models.CharField(max_length=50, blank=True, null=True)
    password_reset_expiry = models.DateTimeField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)
    last_login_ip = models.GenericIPAddressField(blank=True, null=True)

    joined_at = models.DateTimeField(default=timezone.now)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'

    objects = UserManager()

    def __str__(self) -> str:
        return self.email

    # These methods are required for running django admin for custom authentication

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
