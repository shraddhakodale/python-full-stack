def calculateElectronicsGST(a, b):
    subtotal = a + b
    return subtotal + (subtotal * 18 / 100)

def calculateFashionGST(c, d):
    subtotal = c + d
    return subtotal + (subtotal * 13 / 100)


def calculateFoodGST(e):
    return e + (e * 7 / 100)


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c,d)
    food = calculateFoodGST(e)
    
    return electronics + fashion + food

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount

a, b, c, d, e = 100, 100, 100, 100, 100

total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)


print(f"Total after GST = ₹{total:.2f}")
print(f"Discount = ₹{discount:.2f}")
print(f"Final payable amount = ₹{final_amount:.2f}")
