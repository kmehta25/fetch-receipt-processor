from .models import Item
import math
import decimal

def count_alphanumeric(retailer):
    ctr = 0
    for char in retailer:
        if char.isalnum():
            ctr += 1
    
    return ctr

def is_round_int(total):
    if not isinstance(total, decimal.Decimal):
        total = decimal.Decimal(str(total))

    return float(total).is_integer() 


def calculate_points(receipt_obj):
    points = 0

    # Rule #1: 1 point for each alphanumeric char in retailer name
    points += count_alphanumeric(receipt_obj.retailer)

    # Rule #2: 50 points if the total is a round integer

    if is_round_int(receipt_obj.total):
        points += 50
    
    # Rule #3: 25 points if the total is a multiple of 25
    if receipt_obj.total % decimal.Decimal(0.25) == 0:
        points += 25
    
    # Rule #4: 5 points for every 2 items on the receipt
    items_list = Item.objects.filter(receipt = receipt_obj.id)
    if(len(items_list) % 2 == 0):
        points+= int((len(items_list) / 2) * 5)
    else:
        points += int(((len(items_list) - 1) / 2) * 5)

    # Rule #5: If the trimmed length of the item description is a multiple of 3,
    # multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    for item in items_list:
        if len(item.shortDescription.strip()) % 3 == 0:
            points_to_add = int(math.ceil(item.price * decimal.Decimal(0.2).quantize(decimal.Decimal('0.00'))))

            points += points_to_add
    
    # Rule #6: 6 points if the day of purchase is odd
    if receipt_obj.purchaseDate.day % 2 != 0:
        points += 6
    
    # Rule #7: 10 points if the time of purchase is after 2 PM and before 4 PM.
    if receipt_obj.purchaseTime.hour >= 14 and receipt_obj.purchaseTime.hour <= 16:
        points += 10
    

    return points

            

