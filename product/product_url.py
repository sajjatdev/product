from itertools import product
from django.urls import path
from .views import Products,collection
urlpatterns=[
    path("products/",Products.as_view()),
    path("collection/",collection.as_view())
]