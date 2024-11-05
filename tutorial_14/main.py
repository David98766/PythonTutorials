import tkinter as tk
from tkinter import messagebox
from tutorial_14.dao.UserDao import UserDao  # Importing UserDao class for database operations
from tutorial_14.model.User import User  # Importing User class to represent a user object

# Create an instance of UserDao
userDao = UserDao()

# Main Application Class
class App(tk.Tk):  # App inherits from tk.Tk to create the main window
    def __init__(self):
        super().__init__()
        self.title("Login and Sign Up")  # Set the window title
        self.geometry("400x300")  # Set the window size
        self.switch_frame(LoginPage)  # Start the app with the LoginPage

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)  # Create an instance of the new frame
        if hasattr(self, "_current_frame"):  # Check if there is an existing frame
            self._current_frame.destroy()  # Remove the current frame
        self._current_frame = new_frame  # Set the new frame as the current frame
        self._current_frame.pack()  # Display the new frame

# Login Page Class
class LoginPage(tk.Frame):  # LoginPage inherits from tk.Frame to create a frame for login
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # Email Label and Entry
        tk.Label(self, text="Email:").pack(pady=5)  # Label for email input
        self.email_entry = tk.Entry(self)  # Entry widget for email input
        self.email_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(self, text="Password:").pack(pady=5)  # Label for password input
        self.password_entry = tk.Entry(self, show="*")  # Entry widget for password input, masked
        self.password_entry.pack(pady=5)

        # Login Button
        tk.Button(self, text="Login", command=self.login).pack(pady=10)  # Button to trigger login

        # Switch to Sign Up Page
        tk.Button(self, text="Sign Up", command=lambda: master.switch_frame(SignUpPage)).pack(pady=5)  # Button to switch to SignUpPage

    def login(self):
        email = self.email_entry.get()  # Get the email input
        password = self.password_entry.get()  # Get the password input

        # Attempt to retrieve the user with the given email and password
        user = userDao.getUser(email, password)

        if user:  # If a user is found, show success message
            messagebox.showinfo("Login", "Successfully logged in!")
        else:  # If no user is found, show error message
            messagebox.showerror("Login", "Invalid email or password!")

# Sign Up Page Class
class SignUpPage(tk.Frame):  # SignUpPage inherits from tk.Frame to create a frame for sign-up
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        # First Name Label and Entry
        tk.Label(self, text="First Name:").pack(pady=5)  # Label for first name input
        self.first_name_entry = tk.Entry(self)  # Entry widget for first name input
        self.first_name_entry.pack(pady=5)

        # Last Name Label and Entry
        tk.Label(self, text="Last Name:").pack(pady=5)  # Label for last name input
        self.last_name_entry = tk.Entry(self)  # Entry widget for last name input
        self.last_name_entry.pack(pady=5)

        # Email Label and Entry
        tk.Label(self, text="Email:").pack(pady=5)  # Label for email input
        self.email_entry = tk.Entry(self)  # Entry widget for email input
        self.email_entry.pack(pady=5)

        # Password Label and Entry
        tk.Label(self, text="Password:").pack(pady=5)  # Label for password input
        self.password_entry = tk.Entry(self, show="*")  # Entry widget for password input, masked
        self.password_entry.pack(pady=5)

        # Sign Up Button
        tk.Button(self, text="Sign Up", command=self.sign_up).pack(pady=10)  # Button to trigger sign-up

        # Switch to Login Page
        tk.Button(self, text="Back to Login", command=lambda: master.switch_frame(LoginPage)).pack(pady=5)  # Button to switch to LoginPage

    def sign_up(self):
        first_name = self.first_name_entry.get()  # Get the first name input
        last_name = self.last_name_entry.get()  # Get the last name input
        email = self.email_entry.get()  # Get the email input
        password = self.password_entry.get()  # Get the password input

        # Create a new user object without specifying the id
        user = User(None, first_name, last_name, email, password)

        try:
            userDao.addUser(user)  # Try to add the user to the database
            messagebox.showinfo("Sign Up", "User signed up successfully!")  # Show success message
        except ValueError as e:  # Catch any ValueError exceptions (e.g., if the email is already in use)
            messagebox.showerror("Sign Up", str(e))  # Show error message

# Run the Application
if __name__ == "__main__":
    app = App()  # Create an instance of the App class
    app.mainloop()  # Run the main event loop
