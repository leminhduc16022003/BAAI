products = [{"name": "Laptop", "price": 1200, "category": "Electronics"},
{"name": "Shirt", "price": 45, "category": "Clothing"},
{"name": "Phone", "price": 800, "category": "Electronics"},
{"name": "Shoes", "price": 120, "category": "Clothing"},
{"name": "Tablet", "price": 350, "category": "Electronics"},
{"name": "Jacket", "price": 95, "category": "Clothing"},
{"name": "Book", "price": 25, "category": "Books"},
{"name": "Headphones", "price": 150, "category": "Electronics"}]
total_original_price = 0
total_discount_amount = 0
total_final_price = 0
print("=== PRODUCT DISCOUNT CALCULATOR ===")
for product in products:
    name = product["name"]
    price = product["price"]
    category = product["category"]

    discount_percent = 0 
    if category == "Electronics":
        if price >= 1000:
            discount_percent = 0.20  
        elif price >= 500:
            discount_percent = 0.15  
        else:
            discount_percent = 0.10  
    elif category == "Clothing":
        if price >= 100:
            discount_percent = 0.25  
        else:
            discount_percent = 0.15  
    elif category == "Books":
        discount_percent = 0.10
    discount_amount = price * discount_percent
    final_price = price - discount_amount
    total_original_price += price
    total_discount_amount += discount_amount
    total_final_price += final_price
    print(f"\nProduct: {name}")
    print(f" Category: {category}")
    print(f" Original Price: ${price:.2f}")
    print(f" Discount: {int(discount_percent * 100)}%")
    print(f" Final Price: ${final_price:.2f}")
print("\n" + "="*3 + " SUMMARY " + "="*3)
print(f"Total Products: {len(products)}")
print(f"Total Original Price: ${total_original_price:.2f}")
print(f"Total Discount: ${total_discount_amount:.2f}")
print(f"Total Final Price: ${total_final_price:.2f}")