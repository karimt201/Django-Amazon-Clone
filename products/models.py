from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


FLAG_TYPES = (
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature')
)

class Product(models.Model):
    name = models.CharField(_('name'),max_length=120)
    flag = models.CharField(_('flag'),max_length=10,choices=FLAG_TYPES)
    price = models.IntegerField(_('price'),)
    image = models.ImageField(_('image'),upload_to='product')
    sku = models.IntegerField(_('sku'),)
    subtitle = models.TextField(_('subtitle'),max_length=500)
    description = models.TextField(_('description'),max_length=50000)
    tags = TaggableManager()
    Brand = models.ForeignKey('Brand',verbose_name=_('brand'),related_name='Product_brand',on_delete=models.SET_NULL,null=True)
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args , **kwargs) : 
        self.slug = slugify(self.name)
        super(Product,self).save(*args , **kwargs) 

    

class ProductImages(models.Model):
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='product_images',on_delete=models.CASCADE)
    image = models.ImageField(_('image'),upload_to='productimages')



class Brand(models.Model):
    name = models.CharField(_('name'),max_length=120)
    image = models.ImageField(_('image'),upload_to='brand')
    slug = models.SlugField(blank=True,null=True)



    def save(self, *args , **kwargs) : 
        self.slug = slugify(self.name)
        super(Brand,self).save(*args , **kwargs) 



class Review(models.Model):
    user = models.ForeignKey(User,verbose_name=_('user'),related_name='review_user',on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,verbose_name=_('product'),related_name='review_product',on_delete=models.CASCADE)
    review = models.TextField(_('review'),max_length=500)
    rate = models.IntegerChoices(_('rate'),choices = [(i,i) for i in range(1,6)])
    create_at = models.DateTimeField(_('create_at'),default=timezone.now) 
