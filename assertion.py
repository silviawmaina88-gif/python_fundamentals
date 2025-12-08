def calculate_discount(price,discount_percent):
    """calculate discounted price"""
    # assertions to verify input assumptions
    assert price >= 0, "price cannot be negative"
    assert 0 <= discount_percent <= 100, "dicount must be between 0 and 100"
    
    discount_amount= price * discount_percent/100
    final_price= price * discount_amount

    # assertion to verify output
    assert final_price >= 0,"final price cannot be negative"

    return final_price

# valid usage
print(calculate_discount(80,80))