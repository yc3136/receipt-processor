import math
from models import Receipt

def calculate_points(receipt: Receipt) -> int:
    points = 0
    
    # rule 1: 1 point per alphanumeric hcar in retailer name
    points += sum(c.isalnum() for c in receipt.retailer)
    
    # rule 2: 50 points if total is a round dollar amount
    if receipt.total.endswith(".00"):
        points += 50
        
    # rule 3: 25 points if total is multiple of 0.25
    if float(receipt.total) % 0.25 == 0:
        points += 25
    
    # rule 4: 5 points for every 2 items
    points += (len(receipt.items) // 2) * 5

    # rule 5: ceil(price * 0.2) points if item description length is multiple of 3
    for item in receipt.items:
        desc_len = len(item.shortDescription.strip())
        if desc_len % 3 == 0:
            points += math.ceil(float(item.price) * 0.2)
    
    # rule 6: N/A
    
    # rule 7: 6 points if purchase day is odd
    if receipt.purchaseDate.day % 2 == 1:
        points += 6
    
    # rule 8: 10 points if purchase time is between 2pm and 4pm
    hour = receipt.purchaseTime.hour
    if hour == 14 or hour == 15:
        points += 10
    
    return points