from django.db import models
from django.contrib.auth.models import UserManager, Group as RoleModel, PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from rest_framework.pagination import LimitOffsetPagination


class Role(RoleModel):
    class Meta:
        proxy = True


class UserPermissionsMixin(PermissionsMixin):
    groups = None  # remove this field from super class
    user_permissions = None  # remove this field from super class

    role = models.ForeignKey(Role, null=True, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class SimpleUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.is_active = False
        user.is_staff = False
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    password = models.CharField(max_length=20, default=None)
    image = models.URLField(blank=True,
                            default='https://elysator.com/wp-content/uploads/blank-profile-picture-973460_1280-e1523978675847.png')
    address = models.CharField(max_length=600, default='')
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Categorie(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    image = models.URLField(blank=True,
                            default='https://elysator.com/wp-content/uploads/blank-profile-picture-973460_1280-e1523978675847.png')
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Media(models.Model):
    created = models.DateTimeField(default=timezone.now)
    image = models.URLField(blank=True,
                            default='https://elysator.com/wp-content/uploads/blank-profile-picture-973460_1280-e1523978675847.png')

    def __str__(self):
        return str(self.created)


class Product(models.Model):
    category = models.ForeignKey(Categorie, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=500, default='')
    volume = models.TextField(default='')
    address = models.TextField(default='')
    reason_for_selling = models.TextField(default='')
    brand = models.TextField(default='')
    model = models.TextField(default='')
    media = models.ManyToManyField(Media)
    price = models.FloatField(max_length=500, blank=False)
    is_used = models.BooleanField(default=False)
    is_by_admin = models.BooleanField(default=False)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    ordered_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='orderby')
    is_delivered = models.BooleanField(default=False)
    is_cash = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    description = models.CharField(max_length=500, default='')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Post(models.Model):
    description = models.CharField(max_length=500, default='')
    media = models.ManyToManyField(Media, related_name='likffes')
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='likces', default=None, null=True)
    comments = models.ManyToManyField(Comment, related_name='cc', default=None, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.description)


class DefaultPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 10
