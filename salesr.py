def generate_sales_report(sales_data):
    """generate a formated sales report"""
    print('=' * 60)
    print(f"{'MONTHLY SALES REPORT': ^60}")
    print('=' * 60)
    print()
    print(f"{'product': <25} {'quantity': <12} {'price': <11} {'total':<10}")
    print("-" * 60)

    grand_total=0
    for product,quantity,price in sales_data:
        total=quantity * price
        grand_total += total
        print(f"{product: <25} {quantity: <12} ${price: <11.2f} ${total:<10.2f}")
        print('-' * 60)
        print(f"{'grand_total:' :<49} ${grand_total:>9.2f}")
        print('=' * 60)


sales=[
    ("laptop", 5, 899.99),
    ("wireless mouse", 20, 25.50),
    ("usb cable", 50, 5.99),
    ("monitor 24-inch", 8, 199.99)
]
generate_sales_report(sales)

