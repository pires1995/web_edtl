from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group
from django.contrib import auth
from django.utils.translation import gettext, gettext_lazy as _
from django.utils import timezone
import hashlib

# Custom User Manage


class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email Required!')
        if not password:
            raise ValueError('Password Required!')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50, blank=True)
    address = models.CharField(max_length=250, blank=True)
    hashed = models.CharField(max_length=100, blank=True)

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        help_text=(
            ''
        ),
        related_name="user_set",
        related_query_name="user",
    )

    # def get_group_permissions(self, obj=None):
    #     """
    #     Returns a list of permissions that this user has through their groups
    #     """
    #     permissions = set()
    #     for backend in auth.get_backends():
    #         if hasattr(backend, 'get_group_permissions'):
    #             if obj is not None:
    #                 permissions.update(backend.get_group_permissions(
    #                     self, obj
    #                 ))
    #             else:
    #                 permissions.update(backend.get_group_permissions(self))
    #     return permissions
    def save(self, *args, **kwargs):
        self.hashed = hashlib.md5(str(self.id).encode()).hexdigest()
        return super(User, self).save(*args, **kwargs)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['first_name', 'last_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
