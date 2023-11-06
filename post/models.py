from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(null = True, blank = True, upload_to='images/',default = 'coding.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name='post_like',blank=True)
    category = models.ForeignKey('category',on_delete=models.CASCADE,null =True)
    trend = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post", kwargs={"pk": self.pk})
    
    def number_of_likes(self):
        return self.likes.count()
    
class Category(models.Model):
    name = models.CharField(max_length = 150)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    body = models.TextField()
    post = models.ForeignKey(Post,related_name='comments',on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name