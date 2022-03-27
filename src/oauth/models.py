from django.db import models
from django.db.models.fields import EmailField
from django.core.validators import FileExtensionValidator
from ..base.services import get_path_upload_avatar, validate_size_image



class AuthUser(models.Model):
    """User models for our platform
    """
    email        = models.EmailField(max_length=250, unique=True)
    join_date    = models.DateField(auto_now=True)
    user_info    = models.TextField(max_length=500, blank=True, null=True)
    display_name = models.CharField(max_length=30, blank=True, null=True)
    avatar       = models.ImageField(
                        upload_to=get_path_upload_avatar,
                        blank=True,
                        null=True, 
                        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
                    )
    
    @property
    def is_autenticated(self):
        return True

    def __str__(self):
        return str(self.email)

class AuthSocialLink(models.Model):
    """Author social link
    """
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, related_name='social_links')
    link = models.URLField(max_length=100)


    def __str__(self):
        return str(self.user)

     