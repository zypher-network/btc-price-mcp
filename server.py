import asyncio
import json
import os
import signal
import time

import requests
from mcp.server import FastMCP

from dotenv import load_dotenv

load_dotenv()

# Create server
mcp = FastMCP("Get Btc Price", port=os.getenv("PORT"))

@mcp.tool(description="get price from APRO")
async def get_price(feed_id: str, auth: str) -> float:
    timestamp = int(time.time())
    response = requests.get(f"https://live-api.apro.com/api/v1/reports/latest?feedID={feed_id}", headers={
        "Authorization": f"{auth}",
        "X-Authorization-Timestamp": f"{timestamp}"
    })
    data = json.loads(response.text)

    return float(data.get("report", {}).get("midPrice", 0.0))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: ())
    mcp.run(transport="sse")