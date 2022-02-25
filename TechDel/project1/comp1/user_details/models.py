from django.db import models

# Create your models here.
class user_details(models.Model):
    #id=models.
    username = models.CharField(max_length=200,primary_key="true")
    first_name = models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    passw=models.CharField(max_length=200)
    cpass=models.CharField(max_length=200)


class login(models.Model):
	username= models.CharField(max_length=200,primary_key='true')
	password=models.CharField(max_length=200)


class products(models.Model):
    product_id=models.CharField(max_length=10)
    product_type=models.CharField(max_length=200)
    product_name=models.CharField(max_length=1000)
    product_desc=models.CharField(max_length=1000)
    product_price=models.CharField(max_length=200)
    product_pic=models.CharField(max_length=1000)


class cart_contents(models.Model):
    username=models.CharField(max_length=200)
    product_id=models.CharField(max_length=10)
    product_type=models.CharField(max_length=200)
    product_name=models.CharField(max_length=1000)
    product_desc=models.CharField(max_length=1000)
    product_price=models.CharField(max_length=200)
    product_pic=models.CharField(max_length=1000)
    quantity=models.IntegerField()
    status=models.CharField(max_length=100)
    total=models.IntegerField()

class checkout(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    locality=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    zipcode=models.CharField(max_length=10)
    province=models.CharField(max_length=200)
    Phone=models.CharField(max_length=10)
    check_email=models.CharField(max_length=1000)
    #payment=models.CharField(max_length=200)
