from django.contrib import admin
from .models import FoodModel, Category
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','position')
    class Meta:
        model = Category
    

@admin.register(FoodModel)
class FoodAdmin(admin.ModelAdmin):
    list_display = ['id','name_food', 'price']
    list_filter = ['available',]
    class Meta:
        model = FoodModel
    