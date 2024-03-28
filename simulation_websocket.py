import websocket
import json

def on_message(ws, message):
    print("Received acknowledgment:", json.loads(message))

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection established")

    # Create a JSON request
    request_data = {
        "product_name": "Truck Green 02",
        "quantity": 10,
        "price": 25.99,
        "color": "Blue",
        "size": "Medium"
    }

    # Convert JSON request to a string and send
    ws.send(json.dumps(request_data))

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/orders/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
