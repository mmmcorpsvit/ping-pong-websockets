import asyncio
import websockets


async def test_ping_pong():
    async with websockets.connect("wss://localhost:8888") as websocket:
        await websocket.send("ping")
        response = await websocket.recv()
        assert response == "pong"


async def test_reconnect():
    for i in range(5):
        try:
            async with websockets.connect("wss://localhost:8888") as websocket:
                await websocket.send("ping")
                response = await websocket.recv()
                assert response == "pong"
                break
        except websockets.exceptions.WebSocketException:
            await asyncio.sleep(1)


async def test_identify_user():
    async with websockets.connect("wss://localhost:8888") as websocket:
        await websocket.send("identify user123")
        response = await websocket.recv()
        assert response == "user123"


if __name__ == "__main__":
    asyncio.run(test_ping_pong())
    asyncio.run(test_reconnect())
    asyncio.run(test_identify_user())
