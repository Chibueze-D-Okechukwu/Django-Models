from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    



class Post(models.Model):
    Title = models.CharField(maxlength = 200)
    Text = models.TextField()
    Author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now_add=True)
    Published_date = models.DateTimeField() 