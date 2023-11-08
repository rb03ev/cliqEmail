import json
from passlib.context import CryptContext
from authenticate import authenticate_email

pass_context = CryptContext(schemes=["sha256_crypt"])

# Save user data
userdata = {}


def register_user(username, email, password):

    # Encrypt password
    encrypted_password = pass_context.hash(password)

    userdata[username] = {
        "email": email,
        "password": encrypted_password,
    }
    print("Registration success")
    # Store user data in the database

    # define logic to check if user email and username credentials are valid
    confirm = authenticate_email(email)
    if confirm:
        pass
    # and if already in the system, to avoid duplicate
    # data -> this should be defined in the auth area
    # and imported for use here
    # Register the user


def login_user(username, password):
    # Verify user data
    # check if user is already saved
    # if so, echo, success
    if username in userdata:
        encrypted_password = userdata[username]["password"]
        if pass_context.verify(password, encrypted_password):
            return "You are logged in."
        else:
            return "Your credentials are invalid."


# Save user data in db or dict or yaml
with open("userdata.json", "w") as file:
    json.dump(userdata, file, indent=4)

r = login_user, register_user
if __name__ == "__main__":
    print(r)
