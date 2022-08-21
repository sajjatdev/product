from turtle import title
from django.db import models




class Collection(models.Model):
    title = models.CharField(max_length=255,)
    create_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'collection'
        managed = True
     



class Product(models.Model):
    title=models.CharField(max_length=255)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    create_at=models.DateTimeField(auto_now_add=True)
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE,related_name="collection")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'product'
        managed = True