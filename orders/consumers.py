from channels.generic.websocket import AsyncWebsocketConsumer
import json

class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        # Parse the incoming JSON message
        text_data_json = json.loads(text_data)
        service_request = text_data_json.get('service_request')

        # Log the received service request (you can modify this as needed)
        print(f"Received Service Request: {service_request}")

        # Prepare an acknowledgment message
        acknowledgment_message = {
            'acknowledgment': f"Received service request: {service_request}",
        }

        # Send the acknowledgment back to the client
        await self.send(text_data=json.dumps(acknowledgment_message))

    async def disconnect(self, close_code):
        pass
