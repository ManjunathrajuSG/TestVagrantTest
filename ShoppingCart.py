basket = [
    {"product": "Leatherwallet", "unit_price": 1100, "gst_percentage": 18, "quantity": 1},
    {"product": "Umbrella", "unit_price": 900, "gst_percentage": 12, "quantity": 4},
    {"product": "Cigarette", "unit_price": 200, "gst_percentage": 28, "quantity": 3},
    {"product": "Honey", "unit_price": 100, "gst_percentage": 0, "quantity": 2}
]

max_gst_product = max(basket, key=lambda x: x["unit_price"] * x["gst_percentage"] / 100)
print(f"The product with the maximum GST amount is: {max_gst_product['product']}")


min_gst_product = min(basket, key=lambda x: x["unit_price"] * x["gst_percentage"] / 100)
print(f"The product with the minimum GST amount is: {min_gst_product['product']}")


total_amount = sum((item["unit_price"] * (1 + item["gst_percentage"] / 100) * item["quantity"]) for item in basket)
print(f"The total amount to be paid to the shopkeeper is: Rs {total_amount:.2f}")
