from django.db import models
class Post(models.Model):
    text=models.TextField(max_length=100)

    def __str__(self):
        return self.text
# Create your models here.
