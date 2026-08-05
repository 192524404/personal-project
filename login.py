def login(username, password):
    if username == "admin" and password == "admin123":
        return "Login Successful"
    return "Invalid Username or Password"

print(login("admin", "admin123"))