from django.shortcuts import get_object_or_404
from api.serializers import ProductSerializer
from api.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    seriallizer = ProductSerializer(products, many=True)


    return Response(seriallizer.data)
@api_view(['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    seriallizer = ProductSerializer(product)
    return Response(seriallizer.data)