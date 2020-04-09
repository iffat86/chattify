from django.db import models

class signin(models.Model):
    username    = models.CharField(max_length=20)
    password    = models.CharField(max_length=20)
