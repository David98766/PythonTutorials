from Tutorial_13.dao.UserDao import UserDao
from Tutorial_13.model.User import User

class mainUser:
    def __init__(self, userDao):
        self.userDao = userDao  # Correct usage of the userDao instance passed in

    def login(self, email, password):

        # Use both email and password in getUser, and call it from self.userDao
        userToLogin = self.userDao.getUser(email, password)

        if userToLogin:
            return True

        else:
            return False

    def mainUser(self):
        user = User(6, "Jane", "Doe", "Jane@gmail.com", "pw1")
        self.userDao.addUser(user)

        email = input("enter your email: ")
        password = input("enter your password: ")

        if self.login(email, password):
            print("Successfully logged in!")

        else:
            print("Invalid email or password!")

        self.userDao.deleteUser(user.email)


if __name__ == '__main__':
    # Initialize UserDao and pass it to mainUser
    userDao = UserDao()  # Replace this with actual initialization if required
    app = mainUser(userDao)

    # Run the main login function
    app.mainUser()



