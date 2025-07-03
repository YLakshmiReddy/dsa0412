# Item prices and quantities
item_prices = [50, 100, 30]
quantities = [2, 1, 3]

# Discount and tax rates in %
discount_rate = 10  # 10%
tax_rate = 5        # 5%

# 1. Calculate total cost before discount and tax
subtotal = sum(price * qty for price, qty in zip(item_prices, quantities))

# 2. Apply discount
discount_amount = (discount_rate / 100) * subtotal
price_after_discount = subtotal - discount_amount

# 3. Apply tax
tax_amount = (tax_rate / 100) * price_after_discount
total_cost = price_after_discount + tax_amount

# 4. Print results
print(f"Subtotal: ₹{subtotal:.2f}")
print(f"Discount: -₹{discount_amount:.2f}")
print(f"Tax: +₹{tax_amount:.2f}")
print(f"Total cost to be paid: ₹{total_cost:.2f}")
