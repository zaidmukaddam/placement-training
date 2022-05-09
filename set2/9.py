def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    # write your logic here
    if quantity_ordered < 1:
        return -1

    if food_type == "V":
        bill_amount += 120 * quantity_ordered
    elif food_type == "N":
        bill_amount += 150 * quantity_ordered
    else:
        return -1

    if distance_in_kms < 1:
        return -1
    elif 3 < distance_in_kms <= 6:
        bill_amount += (distance_in_kms - 3) * 3
    elif distance_in_kms > 6:
        bill_amount += (distance_in_kms - 6) * 6 + 9

    return bill_amount


# Provide different values for food_type,quantity_ordered,distance_in_kms and test your progra
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)
