from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def profile(self):
        return Profile.objects.get(user=self)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom_enfant = models.CharField(max_length=300)
    genre = models.CharField(max_length=1, choices=[('M', 'Masculin'), ('F', 'Féminin')], default='M')
    ville_residence = models.CharField(max_length=300)
    ville_naissance = models.CharField(max_length=15, unique=True, blank=True, null=True)
    ecole = models.CharField(max_length=15, unique=True, blank=True, null=True)
    classe = models.CharField(max_length=15, unique=True, blank=True, null=True)
    age_enfant = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="user_images", default="default.jpg")
    verified = models.BooleanField(default=False)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
