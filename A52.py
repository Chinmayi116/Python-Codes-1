username = input("Enter username: ")
password = input("Enter password: ")
if username != "admin" or password != "123":
    print("Login Failed")
    exit()      # Terminate program
print("Login Successful")
