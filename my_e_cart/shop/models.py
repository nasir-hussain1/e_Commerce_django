from django.db import models

# Create your models here.
class product(models.Model):
    prod_id = models.AutoField
    prod_subcategory = models.CharField(max_length=30,default='Product Subcategory')
    prod_name = models.CharField(max_length=30, default="")
    prod_desc = models.CharField(max_length=200, default="")
    prod_category = models.CharField(max_length=30, default="")
    prod_subcategory = models.CharField(max_length=30,default="")
    prod_price = models.IntegerField(default=0)
    prod_pub_date =models.DateField()
    prod_image = models.ImageField(upload_to = "shop/images", default="")


    def __str__(self):
        return self.prod_name


