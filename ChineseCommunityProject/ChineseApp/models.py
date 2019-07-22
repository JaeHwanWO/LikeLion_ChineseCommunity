from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length = 200)
    pubDate = models.DateTimeField('date published')
    body = models.TextField()
    nickName = models.CharField(max_length = 20)
    isNotice = models.BooleanField()
    image = models.ImageField()
    #uuid = models.UUIDField()

    