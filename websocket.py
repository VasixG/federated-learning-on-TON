import asyncio
import websockets
import time

async def train_neural_network(websocket, path):
    epochs = 100
    for epoch in range(1, epochs + 1):
        await asyncio.sleep(0.01)  # Simulate time taken for each epoch
        progress = f" {epoch}%"
        print(progress)
        await websocket.send(progress)
    await websocket.send("Training completed")

start_server = websockets.serve(train_neural_network, 'localhost', 65432)


asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
