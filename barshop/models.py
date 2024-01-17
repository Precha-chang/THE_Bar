from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Category(models.Model):
    name = name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    img = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    desc = models.TextField()
    unit = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.IntegerField()

    def __str__(self):
        return self.product.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_code = models.CharField(max_length=10)
    status = models.CharField(max_length=32, choices=(
        ("Wait", "Wait"),
        ("Process", "Process"),
        ("Success", "Success")
    ))
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_code


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.IntegerField()

    def __str__(self):
        return self.product.name
    
class Table (models.Model):
    
    table_id = models.CharField(max_length=3)
    status = models.CharField(max_length=32, choices=(
        ("Wait", "Wait"),
        ("Process", "Process"))
    )
    
class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)

    
    def __str__(self):
        return self.user.username
    
    # class Customer (models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # balance = models.DecimalField(max_digits=20, decimal_places=2)
    # customer_code = models.CharField(max_length=10)


    # def __str__(self):

    #     return self.user.first_name+" "+self.user.last_name


    
    

        
