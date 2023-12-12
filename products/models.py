from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
FLAG_TYPES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature')
)

class Product(models.Model):
    name = models.CharField(max_length=120)
    flag = models.CharField(max_length=10,choices=FLAG_TYPES)
    price = models.IntegerField()
    image = models.ImageField(upload_to='product')
    sku = models.IntegerField()
    subtitle = models.TextField(max_length=500)
    description = models.TextField(max_length=50000)
    tags = TaggableManager()
    Brand = models.ForeignKey('Brand',related_name='Product_brand',on_delete=models.SET_NULL,null=True)





class ProductImages(models.Model):
    product = models.ForeignKey(Product,related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='productimages')



class Brand(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='brand')



class Review(models.Model):
    user = models.ForeignKey(User,related_name='review_user',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,related_name='review_product',on_delete=models.CASCADE)
    review = models.TextField(max_length=500)
    rate = models.IntegerChoices(choices = [(i,i) for i in range(1,6)])
    create_at = models.DateTimeField(default=timezone.now) 
