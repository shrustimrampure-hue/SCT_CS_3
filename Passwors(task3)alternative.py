#Password Strength Checker Program
import re
#Password must be at least 8 character long
password=input("Enter Your Password: ")
if len(password)<8:
    print("Password must be at least 8 characters long.")
#Password must contain at least one uppercase letter
elif not re.search("[A-Z]",password):
    print("Password must contain at laest one uppercase letter.")
#Password must contain at least one lowercase letter
elif not re.search("[a-z]",password):
    print("Password must contain at least one lowercase letter.")
#Password must contain at least one number
elif not re.search("[0-9]",password):
    print("Password must contain at least one number")
else:
    print("Password is strong")