import httpx

async def get_open_orders():
    # Replace with actual API call to Sellbrite
    # Example response structure:
    # {"orders": [{"value": 100}, {"value": 200}], "count": 2}
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.sellbrite.com/orders", headers={"Authorization": "Bearer YOUR_API_KEY"})
        orders = response.json()
        total_value = sum(order["value"] for order in orders["orders"])
        total_count = len(orders["orders"])
    return {"total_count": total_count, "total_value": total_value}
