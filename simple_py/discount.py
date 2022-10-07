# Asks the user for the regular price and the percentage.
regular = input("Regular Price: ")
percent_off = input("Percent Off: ")

# Calculates the price with the discount.
def discount(price, percentage):
    return price * (100 - percentage) / 100

# Set's the sale price with the discount.
sale = discount(float(regular), float(percent_off))

# Prints the sale to the user.
print("Sale Price: " + str(sale) + "$")