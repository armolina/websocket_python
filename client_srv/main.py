import asyncio
import websockets

async def hello():
    async with websockets.connect("ws://server_srv:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        while True:
            print(f"Message received : {message}")

asyncio.run(hello())