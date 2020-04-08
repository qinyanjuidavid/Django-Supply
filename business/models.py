from django.db import models
from accounts.models import User,Categories


class Products(models.Model):
    item=models.CharField(max_length=50)
    category=models.ForeignKey(Categories,on_delete=models.CASCADE)
    price=models.IntegerField(default=0)
    discount_price=models.IntegerField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to=f'Products')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateField(auto_now_add=True)
    date_updated=models.DateField(auto_now=True)


    def __str__(self):
        return self.item
