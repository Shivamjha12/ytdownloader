from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Jobs(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, default="")
    title = models.CharField(max_length=200)
    img = models.CharField(max_length=300, default="")
    video = models.CharField(max_length=300, default="")
    content = models.TextField()
    Description = models.TextField(default=" ")
    price = models.IntegerField(("price"), default="5")
    para2 = models.TextField(default="")
    para3 = models.TextField(default="")
    tags = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email
# def get_profile_image_filepath(self, filename):
#     return f'profile_image/{self.pk}/{"profile_image.png"}'

# class Account(AbstractBaseUser):
#     email                              = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username                           = models.CharField(max_length=30, unique=True)
#     date_joined                        = models.DateTimeField(verbose_name="date_joined", auto_now_add=True)
#     last_login                         = models.DateTimeField(verbose_name="last_login", auto_now_add=True)
#     is_admin                           = models.BooleanField(default=False)
#     is_active                          = models.BooleanField(default=True)
#     is_staff                           = models.BooleanField(default=False)
#     is_superuser                       = models.BooleanField(default=False)
#     profile_image                      = models.ImageField(max_length=230,upload_to=, null=True, default=)

    