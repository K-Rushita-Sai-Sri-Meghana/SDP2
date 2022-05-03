from django.db import models
class User(models.Model):
    username = models.CharField(max_length=100, default="",blank=False)
    email = models.EmailField(max_length=30,default="", blank=False)
    phoneno = models.CharField(max_length=10,default="")
    password = models.CharField(max_length=20,default="", blank=False)
    cpassword = models.CharField(max_length=20, default="", blank=False)
    class Meta:
        db_table = "user"
class Content(models.Model):
    name=models.CharField(max_length=100,blank=False)
    email = models.EmailField(max_length=30,default="", blank=False)
    city=models.CharField(max_length=100,blank=False)
    address= models.CharField(max_length=100, blank=False)
    zip=models.CharField(max_length=20,default="", blank=False)
    class Meta:
        db_table='order_table'

# application/models.py




