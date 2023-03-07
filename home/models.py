from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=45,verbose_name='دسته بندی')
    position = models.PositiveIntegerField(verbose_name='جایگاه')
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
        
    def __str__(self):
        return self.title
class FoodModel(models.Model):
    name_food = models.CharField(max_length=250,verbose_name='نام غذا')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    description = models.CharField(max_length=300, verbose_name='درباره غذا',blank=True, null=True)
    img = models.ImageField(upload_to='images/')
    available  = models.BooleanField(default=True, verbose_name='وضعیت')
    category = models.ForeignKey(to=Category, related_name='category', on_delete=models.SET_NULL,null=True, blank=True)
    
    class Meta:
        verbose_name = 'غذا'
        verbose_name_plural = ' غذا ها'
    def __str__(self):
        return self.name_food
    
    
    