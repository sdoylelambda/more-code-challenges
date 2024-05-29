# Get the Area of a Country

# Create a function that takes a country's name and its area as arguments and returns the area of the
# country's proportion of the total world's landmass.

# The total world's landmass is 148,940,000 [Km^2]
# Round the result to two decimal places.

# UPER

# Understand
# input: String of country name, number of landmass
# output: String with countries name and percent of landmass

# Plan
# Option 1
# percent_of_land = area / 148,940,000
# return string

# Execute
# Option 1
# percent_of_land = area / 148,940,000
# return string

# Revise


def area_of_country(name, area):
    percent_of_land = area / 148940000
    percent_of_land *= 100
    output = f"{name} is {str(round(percent_of_land, 2))}% of the total world's landmass"
    return output


# Examples
area_of_country("Russia", 17098242)  # ➞ "Russia is 11.48% of the total world's landmass"

area_of_country("USA", 9372610)  # ➞ "USA is 6.29% of the total world's landmass"

area_of_country("Iran", 1648195)  # ➞ "Iran is 1.11% of the total world's landmass"
