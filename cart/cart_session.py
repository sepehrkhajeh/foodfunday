from home.models import FoodModel
from django.shortcuts import get_object_or_404
CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
        
    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            food = get_object_or_404(FoodModel,id=int(item['id']))
            item['food'] = food
            item['id'] = food.id
            yield item
    
    
    def total_price(self):
        total = 0
        for item in self.cart.values():
            total+=item['total']
        return total
    def save(self):
        self.session.modified = True
        
    def add(self,food, quantity=1):
        q = int(quantity)
        if q <=0:
            q = 1
        food_id = str(food.id)
        if food_id not in self.cart:
            self.cart[food_id] = {
                'name_food' : food.name_food,
                'price': food.price,
                'total':food.price*q*1000,
                'img': food.img.url,
                'id' : food_id,
                'quantity' : str(q)
            }
            self.save()
        else:
            self.cart[food_id]['quantity'] = str(q)
            self.cart[food_id]['total'] = food.price*q*1000
            self.save()
    def delete(self,pk):
        food_id = str(pk)
        if food_id in self.cart:
            del self.cart[food_id]
            self.save()
    def remove_cart(self):
        del self.session[CART_SESSION_ID]
        
