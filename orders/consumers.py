from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from orders.models import Order, Supplier, Buyer, Product
import json

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'orders'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(text_data)
        data_dict = json.loads(text_data)
        product_name = data_dict.get("product_name", "")
        print (product_name)

        await self.create_order(product_name)

    @sync_to_async
    def create_order(self, product_name):
        # Hardcoded values for design, color, and status
        supplier = Supplier.objects.first()
        buyer = Buyer.objects.first()
        design = "v1"
        color = "Default Color"
        status = "pending"

        try:
            product = Product.objects.get(name=product_name)
            order = Order.objects.create(
                supplier=supplier,
                product=product,
                design=design,
                color=color,
                buyer=buyer,
                status=status
            )
            return f"Order created for {product_name}"
        except Product.DoesNotExist:
            return f"Product {product_name} does not exist"

    async def delivery_message(self, event):
        # Send delivery message back to the WebSocket client
        await self.send(text_data=json.dumps({
            'type': 'delivery_message',
            'message': event['message']
        }))