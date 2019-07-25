from django.db import models

# Create your models here.
class Posting(models.Model):
    title = models.CharField(max_length = 200)
    nickName = models.CharField(max_length = 20)
    pubDate = models.DateTimeField('date published')
    image = models.ImageField(upload_to="photos/", null=True)
    body = models.TextField()
    isNotice = models.BooleanField(null=True)
    #uuid = models.UUIDField()

    def __str__(self):
        return self.title

    