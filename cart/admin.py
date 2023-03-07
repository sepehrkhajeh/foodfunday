from django.contrib import admin
from .models import Orders, OrderItems
# Register your models here.
@admin.action(description='پرداخت کردن')
def make_paid(Orders ,request, queryset):
    queryset.update(is_paid=False)
    
    
@admin.action(description='لغو باطل کردن')
def make_undo(Orders ,request, queryset):
    queryset.update(undo=False)
    
class OrderItemsAdmin(admin.TabularInline):
    model = OrderItems





class OrdersAdmin(admin.ModelAdmin):
    list_display = ['id','user','phone', 'address','total_price' ,'is_paid','date']
    list_filter = ['is_paid',]
    inlines = (OrderItemsAdmin,)
    actions = [make_paid,make_undo]
    
admin.site.register(Orders, OrdersAdmin)