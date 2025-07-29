from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    is_farmer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        
    def __str__(self):
        return self.email

    # Override related names to avoid conflicts with Django's User model
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='custom_user_set',
        related_query_name='custom_user'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_set',
        related_query_name='custom_user'
    )

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    about_me = models.TextField(blank=True, null=True)
    education = models.JSONField(default=list, blank=True)   # [{years, school, desc}]
    experience = models.JSONField(default=list, blank=True)  # [{years, company, desc}]
    skills = models.JSONField(default=list, blank=True)      # ["Python", "Django", ...]
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} Profile"

class VitalSigns(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    temperature = models.FloatField()
    respiratory_rate = models.FloatField()
    spo2 = models.FloatField()
    heart_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
