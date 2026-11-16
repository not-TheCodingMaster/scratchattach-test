import scratchattach

print("Welcome.")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == scratchattach.login(username) and password == scratchattach.login(password):
    print(f"Logged in as {username}")
else:
    print("Invalid credentials. Exiting.")