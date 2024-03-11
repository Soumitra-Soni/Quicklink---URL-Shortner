from django.db import models

# Create your models here.

class QuicklinkApp(models.Model):
    link= models.CharField(max_length=300)
    uid = models.CharField(max_length=100)


    def __str__(self):
        return self.link