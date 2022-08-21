
from django.shortcuts import render,get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Collection,Product
from .ApiSerializer import collectionSerializer,ProductSerializer
# Create your views here.

class Products(APIView):
    def get(self,res):
        query_set=get_list_or_404(Product.objects.select_related("collection").all())
        serializer=ProductSerializer(query_set,many=True)
        return Response(serializer.data)
    def post(self,res):
        Serializer=ProductSerializer(data=res.data)
        Serializer.is_valid(raise_exception=True)
        Serializer.validated_data
        Serializer.save()
        query_set=get_list_or_404(Product.objects.select_related("collection").all())
        getserializer=ProductSerializer(query_set,many=True)
      
        return Response(getserializer.data)

class collection(APIView):

    def post(self,res):
        serializer=collectionSerializer(data=res.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data
        serializer.save()
        query_set=get_list_or_404(Collection.objects.all())
        getserializer=collectionSerializer(query_set,many=True)
        return Response(getserializer.data)
   
    def get(self,res):
        query_set=get_list_or_404(Collection.objects.all())
        getserializer=collectionSerializer(query_set,many=True)
        return Response(getserializer.data)