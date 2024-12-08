from fastapi import FastAPI
from app.platform_clients import sellbrite, ebay, shopify, mercari, etsy

app = FastAPI(title="Middleware API", description="Aggregates open order data from platforms", version="1.0.0")

@app.get("/api/orders", summary="Get total open orders and values for all platforms")
async def get_orders():
    data = {}
    data["Sellbrite"] = await sellbrite.get_open_orders()
    data["eBay"] = await ebay.get_open_orders()
    data["Shopify"] = await shopify.get_open_orders()
    data["Mercari"] = await mercari.get_open_orders()
    data["Etsy"] = await etsy.get_open_orders()
    return data
