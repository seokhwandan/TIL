from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    topic1 = models.CharField(max_length=100)
    topic2 = models.CharField(max_length=100)
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    pick = models.IntegerField()
    content = models.CharField(max_length=150)