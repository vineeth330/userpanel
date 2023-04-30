from django.db import models


# Create your models here.

class studentdb(models.Model):
    Name = models.CharField(max_length=50, null=True, blank=True)
    Age = models.IntegerField(null=True, blank=True)
    Mobile = models.CharField(max_length=50, null=True, blank=True)
    Email = models.CharField(max_length=50, null=True, blank=True)
    Course = models.CharField(max_length=50, null=True, blank=True)
    Address = models.CharField(max_length=50, null=True, blank=True)
    Image = models.ImageField(upload_to="studentprofile", null=True, blank=True)
