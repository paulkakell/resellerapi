import os
import httpx
from typing import Dict, Any

SELLBRITE_API_URL = "https://api.sellbrite.com/v1/orders"
SELLBRITE_API_KEY = os.getenv("SELLBRITE_API_KEY")

async def get_open_orders() -> Dict[str, Any]:
    headers = {
        "Authorization": f"Bearer {SELLBRITE_API_KEY}",
        "Content-Type": "application/json"
    }
    params = {
        "sb_status": "open",
        "limit": 100
    }
    total_count = 0
    total_value = 0.0
    page = 1

    async with httpx.AsyncClient() as client:
        while True:
            params["page"] = page
            response = await client.get(SELLBRITE_API_URL, headers=headers, params=params)
            response.raise_for_status()
            orders = response.json()

            if not orders:
                break

            for order in orders:
                total_count += 1
                total_value += order.get("total", 0.0)

            page += 1

    return {"total_count": total_count, "total_value": total_value}
