import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length < 1:
        password_var.set("Invalid length")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

# GUI Setup
app = tk.Tk()
app.title("Password Generator")

# Entry for password length
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(app, width=5)
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_var = tk.StringVar()
password_label = tk.Label(app, textvariable=password_var, font=('Arial', 12))
password_label.pack(pady=10)

# Start the application
app.mainloop()
