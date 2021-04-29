from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    photo = CloudinaryField('image', null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args=[str(self.id)])