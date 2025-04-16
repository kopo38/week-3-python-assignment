def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        return price - discount
    return price

# Get user input
try:
    original_price = float(input("Enter the original price: "))
    discount_percentage = float(input("Enter the discount percentage: "))
    
    # Calculate final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print result
    if discount_percentage >= 20:
        print(f"Final price after {discount_percentage}% discount: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")
        
except ValueError:
    print("Please enter valid numerical values.")