from django.db import models
from django.utils import timezone
from accounts.models import UserModel
from home.models import FoodModel
from extation.utils import jalali_converter
# Create your models here.
class Orders(models.Model):
    user = models.ForeignKey(to = UserModel, related_name = "items" , on_delete = models.CASCADE,verbose_name="مشتری" )
    phone = models.CharField(max_length=11, verbose_name="شماره تلفن")
    address = models.TextField(max_length = 300, verbose_name="آدرس")
    description = models.TextField(max_length=600, verbose_name="درباره سفارش",blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True , verbose_name="زمان ثبت سفارش")
    total_price = models.PositiveIntegerField(verbose_name="قیمت کل")
    is_paid = models.BooleanField(default=False, verbose_name="وضعیت پرداخت")
    date = models.DateTimeField(verbose_name="زمان ثبت سفارش", auto_now_add=True ,)
    undo = models.BooleanField(default=False, verbose_name="وضعیت فیش")
        
    
    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارش ها'
        ordering = ('created',)
        
    def __str__(self):
        return self.user.name
    
    def date_create(self):
        return jalali_converter(self.date)
    
class OrderItems(models.Model):
    Order = models.ForeignKey(to=Orders, on_delete=models.CASCADE, related_name = 'items')
    food = models.ForeignKey(to=FoodModel, on_delete= models.CASCADE ,related_name = 'items' , verbose_name = 'محصول')
    quantity = models.SmallIntegerField(verbose_name = 'تعداد', )
    price = models.PositiveIntegerField(verbose_name = 'قیمت', )
    def tprice(self):
        return self.food.price*self.quantity*1000

    def name(self):
        return self.food.name_food
    
    