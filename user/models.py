from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#This model is for user signup

class Profile(models.Model):
    ROLE_CHOICES = (
        ('recycler', 'Recycler'),
        ('upcycler', 'Upcycler'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)


    #