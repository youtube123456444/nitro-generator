import random
import string
import time

def generate_random_code():
    # Generate a random 16-character code with letters and digits
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(16))
    return code

if __name__ == "__main__":
    while True:
        # Generate and print a new code every second
        code = generate_random_code()
        print(code)
        time.sleep(1)  # Pause for 1 second
