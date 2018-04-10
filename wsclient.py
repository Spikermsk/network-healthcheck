import asyncio
from websockets import connect
import json

class EchoWebsocket:
    async def __aenter__(self):
        self._conn = connect("ws://rsage.io:8080/unity")
        self.websocket = await self._conn.__aenter__()
        return self

    async def __aexit__(self, *args, **kwargs):
        await self._conn.__aexit__(*args, **kwargs)

    async def send(self, message):
        await self.websocket.send(message)

    async def receive(self):
        return await self.websocket.recv()


async def main():
    async with EchoWebsocket() as echo:

        while True:
            message = {"cmd":"appCmdWithToken","data":{"appName":"CortexAccess","appCmd":"subscribeToTopic","appData":"fakestats"}}


            await echo.send(json.dumps(message))
            print(await echo.receive())  # "Hello!"


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())