from channels.generic.websocket import AsyncWebsocketConsumer,WebsocketConsumer
from channels.db import database_sync_to_async
from home.models import FoodModel

class FoodPaidConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        
    def get_food(self):
        return FoodModel.objects.filter(is_paid=True)

    # def connect(self):
    #     data = await database_sync_to_async(self.get_food())
    #     print(data)
    #     # for i in data:
    #     #     chart_data = ChartSerializer(i).data
    #     #     await self.send(json.dumps({'number': chart_data.number}))
    #     #     print(chart_data)
    #     await self.accept()











# class OrdersConsumer(WebsocketConsumer):
#     def connect(self):
#         self.accept()
        
#     def disconnect(self,close_code):
#         pass
    
#     def receive(self,obj):
#         pass
