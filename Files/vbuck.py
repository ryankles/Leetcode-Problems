def vbucks_to_dollars(vbucks):
    conversion_rate = 9 / 1000  # 9 dollars for 1000 V-Bucks
    dollars = vbucks * conversion_rate
    return dollars

# Taking user input for V-Bucks
vbucks_amount = float(input("Enter the amount of V-Bucks: "))

# Converting V-Bucks to dollars
dollars_amount = vbucks_to_dollars(vbucks_amount)

# Calculating 60% of the dollars amount
sixty_percent_dollars = dollars_amount * 0.5

print(f"{vbucks_amount} V-Bucks is equal to ${dollars_amount:.2f}")
print(f"50% of this amount is ${sixty_percent_dollars:.2f}")
