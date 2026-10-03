import random
import string
import time

def generate_unique_username() -> str:

    # Create unique username by combining the current timestamp with a random string of 4 lowercase letters to exclude collision with existing usernames.

    timestamp = int(time.time())
    random_suffix = "".join(random.choices(string.ascii_lowercase, k=4))
    return f"user_{timestamp}_{random_suffix}"

def generate_test_user_data() -> dict:

    # Generate a dictionary containing test user data with a unique username.

    username = generate_unique_username()
    return {
        "firstName": "Ivan",
        "lastName": "Ivanovich",
        "address": "123 street Test",
        "city": "The City",
        "state": "The State",
        "zipCode": "000000",
        "phone": "00000000000",
        "ssn": "000000000",
        "username": username,
        "password": "Password123",
    }