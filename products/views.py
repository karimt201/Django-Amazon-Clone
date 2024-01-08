from typing import Any
from django.views.generic import ListView , DetailView
from .models import Product  , Review , ProductImages

# queryset : [products] : filter
# context : user
class ProductList(ListView):
    model = Product


# queryset : main data like Product Details
# context : exstra data like reviews and image
class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImages.objects.filter(product=self.get_object())

        return context
