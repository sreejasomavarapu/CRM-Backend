
from django.db import models



# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    CATEGORY=(
        ('Indoor','Indoor'),
        ('Outdoor','Outdoor'),
        
    )
    
    price = models.IntegerField()
    name = models.CharField(max_length=100)
    category=models.CharField(max_length=100,choices=CATEGORY)
    note=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self) -> str:
        return self.name
    
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Out for delivery','Out for delivery'),
        ('Delivered','Delivered'),
    )

    customer= models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,choices=STATUS )
    date_created=models.DateTimeField(auto_now_add=True)
    note=models.CharField(max_length=200, default="this is a note")

    def __str__(self) -> str:
        return str(self.customer.name)

    
