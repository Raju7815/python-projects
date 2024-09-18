import tkinter as tk
import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    if length < 4:
        return "sorry: Length should be at least 4."
    
    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one character from each set
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fills the rest of the password length with random characters from all_characters
    password += [random.choice(all_characters) for _ in range(length - 4)]
    
    # Shuffles the result to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

def on_generate_button_click():
    try:
        length = int(entry_length.get())
        password = generate_password(length)
        label_result.config(text=f"Generated Password: {password}")
    except ValueError:
        label_result.config(text="Error: Please enter a valid number.")

# Creates the main window
root = tk.Tk()
root.title("Password Generator")

# Creates and place widgets
label_prompt = tk.Label(root, text="Enter the desired length of the password (minimum 4 characters):", font=("Arial", 12))
label_prompt.pack(pady=10)

entry_length = tk.Entry(root, font=("Elephant", 14))
entry_length.pack(pady=5)

button_generate = tk.Button(root, text="Generate Password", font=("Elephant", 14), command=on_generate_button_click)
button_generate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Elephant", 14))
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()