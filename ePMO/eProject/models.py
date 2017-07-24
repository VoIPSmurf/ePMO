from django.db import models
from django.contrib.auth.models import User

class UserJustEntity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    entityref = models.IntegerField(default=0)
    
    def __str__(self):
        return self.entityref
    