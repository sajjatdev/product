
from django.contrib import admin
from django.urls import path,include
from product import product_url
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include(product_url),name="Product_api")
]
