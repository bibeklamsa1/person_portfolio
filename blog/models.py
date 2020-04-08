from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_title=models.TextField(max_length=200)
    blog_field=models.TextField()
    time = models.DateTimeField(auto_now=False, auto_now_add=False)