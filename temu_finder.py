import requests
import random

TOKEN = "8759419199:AAGJtdCyd1Q7rUZQ2ZNA3_CuHG_IV-lCElg"
CHAT_ID = "8440025571"

url = "https://www.temu.com/api/search?keyword=gadgets"

response = requests.get(url)
data = response.json()

products = []

for item in data["items"]:
    price = float(item["price"])

    if price < 10:
        products.append({
            "name": item["title"],
            "price": price,
            "image": item["image"],
            "url": item["url"]
        })

random_products = random.sample(products, 5)

for p in random_products:

    message = f"""
🔥 Producto encontrado

🛒 {p['name']}

💰 Precio: ${p['price']}

🔗 {p['url']}
"""

    requests.get(
        f"https://api.telegram.org/bot{TOKEN}/sendPhoto",
        params={
            "chat_id": CHAT_ID,
            "photo": p["image"],
            "caption": message
        }
    )
