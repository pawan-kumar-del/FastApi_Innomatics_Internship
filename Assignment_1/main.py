from fastapi import FastAPI,Query

app = FastAPI()

# ── Temporary data — acting as our database for now ──────────
products = [
    {'id': 1, 'name': 'Wireless Mouse', 'price': 499, 'category': 'Electronics', 'in_stock': True},
    {'id': 2, 'name': 'Notebook', 'price': 99, 'category': 'Stationery', 'in_stock': True},
    {'id': 3, 'name': 'USB Hub', 'price': 799, 'category': 'Electronics', 'in_stock': False},
    {'id': 4, 'name': 'Pen Set', 'price': 49, 'category': 'Stationery', 'in_stock': True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True}, 
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

# Home Endpoint
@app.get('/')
def home():
    return {'message': 'Welcome to our E-commerce API'}

@app.get("/store-info")
def store_info():
    in_stock_count = len([p for p in products if p["in_stock"]])
    out_of_stock_count = len([p for p in products if not p["in_stock"]])
    categories = list(set(p["category"] for p in products))

    return {
        "store_name": "My E-commerce Store",
        "total_products": len(products),
        "in_stock": in_stock_count,
        "out_of_stock": out_of_stock_count,
        "categories": categories
    }


# Return all products
@app.get('/products')
def get_all_products():
    return {'products': products, 'total': len(products)}
@app.get("/products/instock") 
def get_instock(): 
    available = [p for p in products if p["in_stock"] == True] 
    return {"in_stock_products": available, "count": len(available)}

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    result = [p for p in products if keyword.lower() in p["name"].lower()]
    
    if not result:
        return {"message": "No products found"}
    
    return {
        "search_keyword": keyword,
        "results": result,
        "count": len(result)
    }

@app.get("/products/deals")
def get_best_and_premium():
    best_deal = min(products, key=lambda x: x["price"])
    premium_pick = max(products, key=lambda x: x["price"])

    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }
@app.get('/products/{product_id}')
def get_product(product_id: int):
    for product in products:
        if product['id'] == product_id:
            return {'product': product}
    return {'error': 'Product not found'}


@app.get("/products/category/{category_name}") 
def get_by_category(category_name: str): 
    result = [p for p in products if p["category"] == category_name] 
    if not result: 
        return {"error": "No products found in this category"} 
    return {"category": category_name, "products": result, "total": len(result)}