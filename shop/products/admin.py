from django.contrib import admin
from .models import (Product, ProductImage, Tag, Review,
                     ProductSpecification, Sale)

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(ProductSpecification)
admin.site.register(Sale)
