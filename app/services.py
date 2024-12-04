from app.models import Receipt

def calculate_points(receipt: Receipt) -> int:
    """
    Calculate points based on the given receipt.
    """
    points = 0
    
    # Retailer name points
    points += len(receipt.retailer.replace(" ", ""))
    
    # Total amount rules
    if receipt.total[-1] == "0":
        points += 50
    if int(receipt.total.split(".")[1]) % 25 == 0:
        points += 25
    
    # Item-based rules
    points += (len(receipt.items) // 2) * 5
    for item in receipt.items:
        if len(item.shortDescription.strip()) % 3 == 0:
            points += int(float(item.price) * 0.2)
    
    # Date and time-based rules
    if receipt.purchaseDate[-1] in "02468":
        points += 6
    purchase_hour = int(receipt.purchaseTime.split(":")[0])
    
    if 14 <= purchase_hour < 16:
        points += 10
    
    return points
