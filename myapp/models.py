from django.db import models
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Entry(models.Model):
    name = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date =  models.DateTimeField()
    description = models.TextField()
    gambar = models.FileField(blank=True ,null=True)
    lacations= models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
        #return f'{self.name} {self.date}'
