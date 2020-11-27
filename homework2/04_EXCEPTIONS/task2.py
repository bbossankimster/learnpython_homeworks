def discounted(price, discount):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
    except ValueError:
        return print('Введены некорректные данные.')
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    print(price_with_discount)

price2 = 100
discount2 = 80
discounted(price2, discount2)
print("Finish!")


price2 = "sad"
discount2 = 80
discounted(price2, discount2)
print("Finish!")
   