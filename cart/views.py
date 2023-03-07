from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import View
from django.http import JsonResponse,Http404
from home.models import FoodModel
from .cart_session import Cart
from .forms import OrderForm
from .models import Orders,OrderItems
# Create your views here.

def cart_details(request):
    cart = Cart(request)
    return render(request,"cart/cart_detail.html", {'cart': cart})
    


def food_details(request,pk):
    foods = FoodModel.objects.get(pk=pk)
    return render(request,"home/fooddetails.html", {'food': foods})
class CartAddView(View):
    def post(self, request):

        quantity = request.POST.get('quantity')
        food_id = request.POST.get('id')
        food = FoodModel.objects.get(pk=food_id)
        cart = Cart(request)
        cart.add(food,quantity)

        return JsonResponse({'key':'success'})

class DeleteCartView(View):

    def get(self, request, pk):
        cart = Cart(request)
        cart.delete(pk)
        return JsonResponse({'key':'success'})


class OrderCreateView(View):
    
    def post(self, request):

        address = request.POST['address']
        cart = Cart(request)
        price = cart.total_price()
        if address != "طبقه بالا هستم" and address != "خودم میام تحویل میگیرم":
            price +=15000
        order = Orders.objects.create(user=request.user ,phone=request.user.phone, total_price=price,address=request.POST.get('address'),description=request.POST.get('description'))
        for item in cart:
            OrderItems.objects.create(Order=order,
                                food=FoodModel.objects.get(id=int(item['id'])),
                                price=int(item['price']),
                                quantity=item['quantity'],
                                
                                )
        cart.remove_cart()
        return redirect('cart:order_details',order.pk)


class OrderDetailView(View):
    def get(self, request,pk):
        obj = get_object_or_404(Orders,pk=pk)
        return render(request,"cart/order_details.html", {"order":obj})
    
    def dispatch(self, request,pk):
        obj = get_object_or_404(Orders,pk=pk)
        if request.user == obj.user:
            return self.get(request,pk)
        else:
            raise Http404

class MyOrdersView(View):
    
    def get(self, request):
        query = Orders.objects.filter(user=request.user).order_by('-date')
        return render(request,"cart/listorders.html", {"orders":query})

class OrdersInfo(View):

    def get(self, request,pk):
        obj = get_object_or_404(Orders,pk=pk)
        return render(request,"cart/fish.html", {"order":obj})
    
    def dispatch(self, request,pk):
        obj = get_object_or_404(Orders,pk=pk)
        if request.user == obj.user or request.user.is_admin:
            return self.get(request,pk)
        else:
            raise Http404
            

class PaidOrdersView(View):
    
    def get(self, request):
        list_order = Orders.objects.filter(is_paid=True,undo=False).order_by('-date')
        return render(request,"cart/paidorders.html", {"orders":list_order})
    def dispatch(self, request):

        if request.user.is_admin:
            return self.get(request)
        else:
            raise Http404
            
            
# باطل کردن فیش
def undo_orders(request,pk):
    obj = Orders.objects.get(pk=pk)
    obj.undo = True
    obj.save()
    return JsonResponse({'message':'success'})