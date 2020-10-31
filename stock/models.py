from django.db import models

# Create your models here....


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    product_detail = models.TextField()
    product_barcode = models.CharField(max_length=32)
    product_qty = models.IntegerField()
    product_price = models.DecimalField(decimal_places=2, max_digits=7)
    product_image = models.CharField(max_length=64)
    product_status = models.IntegerField()
    b_date = models.CharField(max_length=8)
    b_code = models.CharField(max_length=8)
    b_withdrawal =models.DecimalField(max_digits=7, decimal_places=2)
    b_deposit = models.DecimalField(max_digits=7, decimal_places=2)
    b_balance = models.DecimalField(max_digits=9, decimal_places=2)
    b_staffid = models.CharField(max_length=4)
