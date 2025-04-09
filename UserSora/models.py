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
        
class ageUser_tb(models.Model):
    ageUser = models.CharField(max_length = 255, verbose_name = 'Age User')
    
    def __str__(self):
        return self.ageUser
    
class educationLevelUser_tb(models.Model):
    educationUser = models.CharField(max_length = 255, verbose_name = 'Education User')
    def __str__(self):
        return self.educationUser
    
class relationKindUser_tb(models.Model):
    relationUser = models.CharField(max_length = 255, verbose_name = 'Relation User' )
    
    def __str__(self):
        return self.relationUser
    
class workUser_tb(models.Model):
    workUser = models.CharField(max_length = 255, verbose_name = 'Work User')
    def __str__(self):
        return self.workUser
class rangeSalary_tb(models.Model):
    salaryUser = models.CharField(max_length = 255, verbose_name = 'Salary User' )
    def __str__(self):
        return self.salaryUser    
class User(AbstractBaseUser, PermissionsMixin):    
    email = models.EmailField(max_length=250, unique=True, verbose_name='Email User')
    password = models.CharField(max_length = 300, verbose_name='User Password')
        
    ageUser = models.ForeignKey(ageUser_tb, on_delete = models.CASCADE, null = True, blank = True)
    educationUser = models.ForeignKey(educationLevelUser_tb, on_delete = models.CASCADE, null = True, blank = True)
    relationUser = models.ForeignKey(relationKindUser_tb, on_delete = models.CASCADE, null = True, blank = True)
    workUser = models.ForeignKey(workUser_tb, on_delete = models.CASCADE, null = True, blank = True)
    salaryUser = models.ForeignKey(rangeSalary_tb, on_delete = models.CASCADE, null = True, blank = True)    
    manyKid = models.CharField(max_length = 250, verbose_name = 'Many Kids', null = True, blank = True)
    
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