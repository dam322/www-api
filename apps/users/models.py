from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(
            email=self.normalize_email(email),
            **kwargs,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **kwargs):
        user = self.create_user(email, password, **kwargs)
        user.type = User.UserType.ADMIN
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.birthday = now()
        user.save()
        return user


class User(AbstractBaseUser):
    class UserType(models.Choices):
        ADMIN = 'admin'
        EMPLOYEE = 'employee'
        CUSTOMER = 'customer'

    email = models.EmailField(max_length=60, unique=True)
    type = models.CharField(choices=UserType.choices, default=UserType.CUSTOMER, null=False, max_length=16)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    cell_phone = models.CharField(max_length=16)
    birth_day = models.DateField(null=True)
    direction = models.CharField(max_length=64)
    city = models.CharField(max_length=32)
    # Información para extender AbstractBaseUser
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    class Meta:
        ordering = ['type']

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
