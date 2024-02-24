products = ["t-shirt", "mug", "hat", "book", "keychain"]

inventory = dict()

for prod in products:
    inventory[prod] = int(input(f"{prod} quantity? in numbers: "))

print("\n\n",inventory,"\n\n",)

customer_orders = set()

for i in range(3):
    prod = input(f"select your product: {products}")
    customer_orders.add(prod)

print(customer_orders)

print(len(customer_orders))

total_products_ordered = len(customer_orders)
total_productos_available = len(products)
percentage_products_ordered = (total_products_ordered / total_productos_available) * 100
order_status = (total_products_ordered, percentage_products_ordered)

print(
f"""
Order Statistics:
Total Products Ordered: {total_products_ordered}
Percentage of Products Ordered: {percentage_products_ordered}
"""
)

for prod in customer_orders:
    inventory[prod] -= 1

print(inventory)
