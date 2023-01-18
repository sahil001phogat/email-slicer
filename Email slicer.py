# Get the email address from the user
email = input("Enter your email address: ")

# Split the email address into username and domain
username, domain = email.split("@")

# Convert domain to uppercase
domain = domain.upper()

# Print the username and domain
print("username:", username,"and","Domain:", domain)