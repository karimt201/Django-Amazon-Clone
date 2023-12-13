from django.contrib import admin
from .models import Product , Brand , ProductImages , Review


class ProductImageInline(admin.TabularInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline ]

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)


# Register your models here.
