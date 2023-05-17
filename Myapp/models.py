from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
# Create your models here.
User = get_user_model()
# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=255)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio = models.CharField(max_length=255, blank=True ,default='Hi ! I am using Dget media')
    location = models.CharField(max_length=255, blank=True)
    birth_date = models.DateField(blank=True,default=None,null=True)
    profileimage = models.ImageField(upload_to='profile_pics/',default='profile.jpg')

    def __str__(self):
        return self.user.username

class Post(models.Model):
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images/')
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    nos_likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4)
    text = models.TextField()
    File = models.FileField(upload_to='file/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    audio = models.FileField(upload_to='audios/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

# class ProfilePic(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
#     pic = models.ImageField(upload_to='profile_pics/')

# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    def __str__(self):
        return self.user

class Like(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username