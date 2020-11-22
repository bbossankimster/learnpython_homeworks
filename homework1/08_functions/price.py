def discounted(price, discount):
    price = abs(float(price))
    discount = abs(float(discount))
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)

price2 = 100
discount2 = 80
discounted(price2, discount2)
print("Finish!")
   