import string
import secrets

# List of possible characters for the password
chars = string.ascii_letters + string.digits + string.punctuation

# Length of the password
password_length = 16

# Ask the user for the site/application and username/email
site = input("Enter the site or application: ")
username = input("Enter the username or email: ")

# Generate the password
password = ''.join(secrets.choice(chars) for i in range(password_length))

# Save the password to a file
with open("passwords.txt", "a") as file:
  file.write(f"{site},{username},{password}\n")

# Print the password
print(f"Your password for {site} ({username}) is: {password}")
