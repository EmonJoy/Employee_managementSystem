from django.db import models

# Create your models here.

class Emp(models.Model):
    name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    address=models.CharField(max_length=150)
    working=models.BooleanField(default=True)
    department=models.CharField(max_length=10)


    def __str__(self):
        return self.name + " | " + self.email_id
