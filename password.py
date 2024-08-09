import random
def generate_password(characters, length=16):
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

pw = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?"

password = generate_password(pw, 16)

print("Do you want to use the password generator or set your own password?")
user_choice = input("Enter 'generator' or 'set': ")
if user_choice != "set" and user_choice !="generator": raise Exception("Invalid input. Please enter 'generator' or 'set'.")
if user_choice == "generator":
    password = generate_password(pw, 16)
    print("Your new password is: ", password)
else:
    print("Dear user, please set a password for your account.")
    user_password = input("Enter your password: ")
    def contains_uppercase(user_password):
        return any(char.isupper() for char in user_password)
    def contains_number(user_password):
        return any(char.isdigit() for char in user_password)
    def contains_special(user_password):
        specialchars="!@#$%^&*()_+-=[]}{|;:,.<>?"
        return any(char in specialchars for char in user_password)
    
    def correct_password(user_password):
        if len(user_password) >= 8 and contains_special(user_password) and contains_uppercase(user_password) and contains_number(user_password):
            return True
        else:
            return False
    while correct_password(user_password) == False:           
        print("Your password must be at least 8 characters long and should include at least 1 uppercase character 1 number and 1 special character.Please try again.")
        user_password = input("Enter your password: ")
        if correct_password(user_password) == True:
            password = user_password
            print("Your password has been successfully set.")
            break