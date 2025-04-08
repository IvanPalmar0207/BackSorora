from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email: 
            raise ValueError('Email must not be empty')
    
        email = self.normalize_email(email)
        user = self.model(email = email, password = password, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        
        return user

    def create_user(self, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self._create_user(email, password, **extra_fields)
        
class User(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(max_length=250, unique=True, verbose_name='Email User')
    password = models.CharField(max_length = 300, verbose_name='User Password')
        
    age = models.CharField(max_length = 250, verbose_name = 'User Age', null=True)
    educationLevel = models.CharField(max_length = 250, verbose_name = 'Education Level', null = True)    
    relationKind = models.CharField(max_length = 250, verbose_name = 'Relation Kind', null = True)
    haveKids = models.BooleanField(max_length = 250, verbose_name = 'Have Kids', null = True )
    workSituation = models.CharField(max_length = 250, verbose_name = 'Work Situation', null = True )
    salaryRange = models.CharField(max_length = 250, verbose_name = 'Salary Range', null = True)
    
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)
    
    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)
    
    objects = CustomUserManager()    
    
    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = ['password']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    