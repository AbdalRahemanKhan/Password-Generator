# Import necessary modules
import random # For generating random characters
import string # For accessing sets of characters

# Define function to generate password
def generate_password(length, complexity):
    # Define the set of characters to choose from based on the desired complexity level
    if complexity == 'low':
        chars = string.ascii_lowercase # Only lowercase letters
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits # Lowercase and uppercase letters plus digits
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation # Lowercase and uppercase letters plus digits and punctuation
    else:
        return 'Invalid complexity level' # Return an error message if the desired complexity level is invalid

    # Generate the password by choosing random characters from the set of characters
    password = '' # Initialize an empty string to hold the password
    for i in range(length): # Loop through the desired length of the password
        password += random.choice(chars) # Add a randomly chosen character from the set of characters to the password

    # Return the generated password
    return password

# Prompt the user for the desired length and complexity level of the password
length = int(input("Enter desired password length: "))
complexity = input("Enter password complexity level (low, medium, high): ")

# Call the generate_password function with the user's desired length and complexity level
password = generate_password(length, complexity)

# Print the generated password to the console
print("Your password is: ", password)
