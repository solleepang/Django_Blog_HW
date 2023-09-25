from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        유저아이디, 이메일, 이름, 닉네임, 비밀번호 받아 User 인스턴스 생성
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        유저아이디, 이메일, 이름, 닉네임, 비밀번호 받아 User 인스턴스 생성,
        최상위 권한 부여
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email address',
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name=('User name'),
        max_length=30,
        unique=True
    )
    fullname = models.CharField(
        verbose_name=('Full name'),
        max_length=30,
        null=True,
    )
    nickname = models.CharField(
        verbose_name=('Nickname'),
        max_length=30,
        unique=True,
    )
    join_date = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_of_birth = models.DateField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

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
