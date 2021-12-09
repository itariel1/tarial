from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.FileField(upload_to="post_images/")
    likes = models.IntegerField(default=0)
    reposts = models.IntegerField(default=0)

class Comment(models.Model):
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
