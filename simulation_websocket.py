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

    # Send a service request
    service_request = {
        'order': 'Some data to process',
    }
    ws.send(json.dumps(service_request))

if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/service/",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open

    ws.run_forever()
