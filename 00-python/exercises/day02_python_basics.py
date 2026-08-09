product_name = input("Enter the product name: ")
unit_price = float(input("Enter the unit price: "))
quantity = int(input("Enter the quantity: "))
discount_percentage = float(input("Enter the discount percentage: "))


subtotal = unit_price * quantity
discount = subtotal * discount_percentage / 100
final_total = subtotal - discount

print(
    f"{quantity} x {product_name} @ {unit_price:.2f} EGP = {final_total:.2f} after {discount_percentage:g}% discount"
)
