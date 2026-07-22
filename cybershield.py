"""
CyberShield - Cyber Security Toolkit
A simple Tkinter-based GUI application with three modules:
1. Password Strength Checker
2. Password Generator
3. Phishing URL Detector
"""

import tkinter as tk
import random
import string

# ======================================================
# Main Window Setup
# ======================================================
window = tk.Tk()
window.title("CyberShield")
window.geometry("700x500")
window.resizable(False, False)
window.configure(bg="white")

# ---------------- Heading ----------------
heading = tk.Label(
    window,
    text="CyberShield",
    font=("Arial", 24, "bold"),
    bg="white",
    fg="darkblue"
)
heading.pack(pady=(30, 5))

# ---------------- Sub Heading ----------------
subheading = tk.Label(
    window,
    text="Cyber Security Toolkit",
    font=("Arial", 14),
    bg="white",
    fg="black"
)
subheading.pack()

# ---------------- Description ----------------
description = tk.Label(
    window,
    text="This application helps users perform basic cyber security checks.",
    font=("Arial", 11),
    bg="white",
    fg="gray"
)
description.pack(pady=15)


# ======================================================
# Module 1: Password Strength Checker
# ======================================================
def open_password_checker():
    password_window = tk.Toplevel(window)
    password_window.title("Password Strength Checker")
    password_window.geometry("500x300")
    password_window.configure(bg="white")

    heading = tk.Label(
        password_window,
        text="Password Strength Checker",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="darkblue"
    )
    heading.pack(pady=20)

    password_label = tk.Label(
        password_window,
        text="Enter Password:",
        font=("Arial", 12),
        bg="white"
    )
    password_label.pack(pady=10)

    password_entry = tk.Entry(
        password_window,
        width=30,
        font=("Arial", 12),
        show="*"
    )
    password_entry.pack(pady=10)

    result = tk.Label(
        password_window,
        text="",
        font=("Arial", 12, "bold"),
        bg="white"
    )
    result.pack(pady=10)

    def check_password():
        password = password_entry.get()
        if len(password) < 6:
            result.config(text="Weak Password", fg="red")
        elif len(password) < 10:
            result.config(text="Medium Password", fg="orange")
        else:
            result.config(text="Strong Password", fg="green")

    check_button = tk.Button(
        password_window,
        text="Check Password",
        font=("Arial", 12),
        bg="lightblue",
        command=check_password
    )
    check_button.pack(pady=15)


# ======================================================
# Module 2: Password Generator
# ======================================================
def open_generator():
    generator_window = tk.Toplevel(window)
    generator_window.title("Password Generator")
    generator_window.geometry("500x300")
    generator_window.configure(bg="white")

    heading = tk.Label(
        generator_window,
        text="Password Generator",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="darkgreen"
    )
    heading.pack(pady=20)

    password_box = tk.Entry(
        generator_window,
        width=30,
        font=("Arial", 12)
    )
    password_box.pack(pady=10)

    def generate_password():
        characters = string.ascii_letters + string.digits + "!@#$%^&*"
        password = "".join(random.choice(characters) for i in range(12))
        password_box.delete(0, tk.END)
        password_box.insert(0, password)

    generate_button = tk.Button(
        generator_window,
        text="Generate Password",
        font=("Arial", 12),
        bg="lightgreen",
        command=generate_password
    )
    generate_button.pack(pady=15)


# ======================================================
# Module 3: Phishing URL Detector
# ======================================================
def open_phishing_detector():
    phishing_window = tk.Toplevel(window)
    phishing_window.title("Phishing URL Detector")
    phishing_window.geometry("500x300")
    phishing_window.configure(bg="white")

    heading = tk.Label(
        phishing_window,
        text="Phishing URL Detector",
        font=("Arial", 16, "bold"),
        bg="white",
        fg="darkred"
    )
    heading.pack(pady=20)

    url_label = tk.Label(
        phishing_window,
        text="Enter URL:",
        font=("Arial", 12),
        bg="white"
    )
    url_label.pack()

    url_entry = tk.Entry(
        phishing_window,
        width=40,
        font=("Arial", 12)
    )
    url_entry.pack(pady=10)

    result = tk.Label(
        phishing_window,
        text="",
        font=("Arial", 12, "bold"),
        bg="white"
    )
    result.pack(pady=10)

    def check_url():
        url = url_entry.get()
        if "https://" in url:
            result.config(text="Looks Safe", fg="green")
        else:
            result.config(text="Suspicious URL", fg="red")

    check_button = tk.Button(
        phishing_window,
        text="Check URL",
        font=("Arial", 12),
        bg="lightyellow",
        command=check_url
    )
    check_button.pack(pady=15)


# ======================================================
# Main Menu Buttons
# ======================================================
password_button = tk.Button(
    window,
    text="Password Strength Checker",
    font=("Arial", 12),
    width=30,
    height=2,
    bg="lightblue",
    command=open_password_checker
)
password_button.pack(pady=10)

generator_button = tk.Button(
    window,
    text="Password Generator",
    font=("Arial", 12),
    width=30,
    height=2,
    bg="lightgreen",
    command=open_generator
)
generator_button.pack(pady=10)

phishing_button = tk.Button(
    window,
    text="Phishing URL Detector",
    font=("Arial", 12),
    width=30,
    height=2,
    bg="lightyellow",
    command=open_phishing_detector
)
phishing_button.pack(pady=10)

# ======================================================
# Run the Application
# ======================================================
if __name__ == "__main__":
    window.mainloop()
