# Ask user for their name
name = input("What's your name? ")

# Remove whitespace from str
# name = name.strip()

# Capitalize user's name - only first word uppercase
# name = name.capitalize()

# Capitalize user's name - all words
# name = name.title()

# Remove whitespace from str and capitalize user's name
name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

#Say hello to user
print(f"hello, {first} + {last}")
