print("===== RESTAURANT MENU =====")


item = input("Enter your item: ")
price = input("Enter the price: ")

dash = 30 - len(item) - len(price)

print(f"{'Item':<20}{'Price':>10}")
print(item + ("-" * dash) + price)
