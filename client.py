import asyncio
from mcp.client.sse import sse_client
from mcp import ClientSession
import os
from dotenv import load_dotenv

async def main():
    load_dotenv()
    async with sse_client(f'http://127.0.0.1:{os.getenv("PORT")}/sse') as streams:
        async with ClientSession(*streams) as session:
            await session.initialize()

            res = await session.call_tool('get_price', {'feed_id': os.getenv('FEEDID'), 'auth': os.getenv('AUTH')})
            print(res)


if __name__ == '__main__':
    asyncio.run(main())