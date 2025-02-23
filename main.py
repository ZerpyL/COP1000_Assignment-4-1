"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = 35.00        
numChars = 20  
color = "gold"       
woodType = "pine"    


# Write assignment and if statements here as appropriate.
if numChars > 5:
    charge += (numChars - 5) * 4 


if woodType == "oak":
    charge += 20.00  
elif woodType == "pine":
    pass  

if color == "gold":
    charge += 15.00

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
