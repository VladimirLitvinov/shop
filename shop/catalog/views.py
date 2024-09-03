from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer
from .utils import filter_catalog, sort_products

from products.serializers import ProductSerializer
from products.models import Product


class Catalog(APIView):

    def get(self, request: Request):
        products = filter_catalog(request)
        products = sort_products(request, products)
        serialized = ProductSerializer(products, many=True)
        return Response({"items": serialized.data})


class BannersList(APIView):
    def get(self, request: Request):
        fav_categories = [obj.pk for obj in
                          Category.objects.filter(favourite=True)]
        banners = Product.objects.filter(category_id__in=fav_categories)

        serialized = ProductSerializer(banners, many=True)
        return Response(serialized.data)


class CategoriesList(APIView):
    def get(self, request: Request):
        categories = Category.objects.filter(parent=None)
        serialized = CategorySerializer(categories, many=True)
        return Response(serialized.data)



