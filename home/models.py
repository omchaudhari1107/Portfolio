from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30,null=False)
    email = models.EmailField(null=False)
    co_no = models.CharField(max_length=12,null=False)
    comment = models.TextField(null=False)