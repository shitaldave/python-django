from django.db import models
from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    # Add any additional fields or customizations to the User model
    # Example fields:
    userid = models.CharField(max_length=50, default="A10", primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    # ...

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    # Add any additional fields or customizations to the Post model
    # Example fields:
    # is_public = models.BooleanField(default=True)
    # ...

class Like(models.Model):
    like_id = models.CharField(max_length=50, default="A10", primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any additional fields or customizations to the Like model
    # Example fields:
    # created_at = models.DateTimeField(auto_now_add=True)
    # ...


