from django.db import models

# Create your models here.
class Item(models.Model):
    item_name = models.CharField(max_length=32, unique=True,verbose_name='상품 이름')
    item_price = models.IntegerField(verbose_name='상품 가격')
    item_image = models.ImageField(upload_to='media',blank=True, null=True)

    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name = '상품'
        verbose_name_plural = '상품'

class Topping(models.Model):
    item_name = models.ForeignKey('Item',on_delete=models.CASCADE, verbose_name='상품 이름')
    topping_name = models.CharField(max_length=32, unique=True,verbose_name='토핑 이름')
    topping_price = models.IntegerField(verbose_name='토핑 가격')

    def __str__(self):
        return self.topping_name
    
    class Meta:
        verbose_name = '토핑'
        verbose_name_plural = '토핑'
