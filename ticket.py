#!/bin/bash

# Define the price of a single ticket
TICKET_PRICE = 100

# Get the ages of the passengers as input
ages = [int(input(f"Enter the age of passenger {i+1}: ")) for i in range(5)]

# Calculate the total price of the tickets, accounting for free tickets for children under 3
total_price = sum([TICKET_PRICE if age >= 3 else 0 for age in ages])

# Output the total price
print(f"The total price of the tickets is ${total_price}.")
