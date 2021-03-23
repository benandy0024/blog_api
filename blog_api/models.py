from django.db import models
from django.conf import settings
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title=models.CharField(max_length=120)
    description=models.TextField(max_length=120,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title