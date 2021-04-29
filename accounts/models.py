from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from cloudinary.models import CloudinaryField

from main.models import Team

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    image = CloudinaryField('image', null=True)
    bio = models.TextField(max_length=500, blank=True)
    course = models.CharField(max_length=30, blank=True)
    reg_no = models.CharField(max_length=20, blank=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('', args=[str(self.id)])


#@receiver(post_save, sender=User)
