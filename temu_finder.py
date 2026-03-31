import requests
import random

TOKEN = "8759419199:AAGJtdCyd1Q7rUZQ2ZNA3_CuHG_IV-lCElg"
CHAT_ID = "8440025571"

url = "https://www.temu.com/api/search?keyword=gadgets"

response = requests.get(url)
data = {
    "items": [
        {"title":"Mini selladora","price":"2.5","image":"https://i.imgur.com/abc.jpg","url":"https://temu.com/product1"},
        {"title":"Organizador de cables","price":"1.8","image":"https://i.imgur.com/def.jpg","url":"https://temu.com/product2"},
        {"title":"Soporte celular","price":"3.2","image":"https://i.imgur.com/ghi.jpg","url":"https://temu.com/product3"},
        {"title":"Mini linterna","price":"2.0","image":"https://i.imgur.com/jkl.jpg","url":"https://temu.com/product4"},
        {"title":"Batería portátil","price":"5.5","image":"https://i.imgur.com/mno.jpg","url":"https://temu.com/product5"},
        {"title":"Llavero multifunción","price":"0.99","image":"https://i.imgur.com/pqr.jpg","url":"https://temu.com/product6"}
    ]
}

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
