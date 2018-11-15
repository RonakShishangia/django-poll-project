from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=50)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"  