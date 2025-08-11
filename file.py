import random
import string

# Character pool for password generation
characters = string.ascii_letters + string.digits + string.punctuation
password_length = 12

print("Welcome to the Password Manager!")
print("Press 1 to add a new account")
print("Press 2 to view all saved accounts")
print("Press 3 to exit")

choice = input("Enter your choice: ")

if choice == '1':
    print("\nYou chose to add a new account.")
    app_name = input("Enter the application name or website name: ")
    user_name = input("Enter the username: ")
    password = input("Enter the password OR press Enter to generate a random one: ")

    # Generate random password if left blank
    if password == "":
        password = ''.join(random.choices(characters, k=password_length))
        print("Your generated password is:", password)

    # Save account details to file (append mode)
    with open("passwords.txt", "a") as f:
        f.write(f"Application: {app_name}\n")
        f.write(f"Username: {user_name}\n")
        f.write(f"Password: {password}\n")
        f.write("-" * 20 + "\n")

    print("Account saved successfully!")

elif choice == '2':
    print("\nYou chose to view all saved accounts.\n")
    try:
        with open("passwords.txt", "r") as f:
            content = f.read()
            if content.strip() == "":
                print("No accounts found in the file.")
            else:
                print(content)
    except FileNotFoundError:
        print("No saved accounts found. The file does not exist yet.")

elif choice == '3':
    print("Exiting the program. Goodbye!")

else:
    print("Invalid choice! Please select 1, 2, or 3.")
