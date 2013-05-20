class Shell:

    def __init__(self):
        self.users = {} ##Users dictionary(key=user-name, value=object-user)
        self.currentUser = None #User who is using the shell,
                                #      it is set at 'login'
        self.validCommands = {'login': self.login, 'logout': self.logout,
                              'exit': self.exit, 
                              'addUser': self.addUser,
                              'whoAmI': self.whoAmI, 'setAdmin': self.setAdmin,
                              'changeCurrentUserPW': self.changeCurrentUserPW,
                              'changeUserPW': self.changeUserPW}

    def addAdmin(self, user):
        """It is use for first time to add an admin to the shell.
		An already admin user is add to the users dictionary.
        """
        if user.isAdmin:
            self.updateUser(user.name, user)
        else: raise Exception("User is not an admin")

    def addUser(self, user):
        """It can only be used by a logged in admin.
		 to add a new user to the user dictionary.
        """
        if self.currentUser.isAdmin:
            self.users.update({user.name:user})
        else: loggin.info("Current user is not an admin")

    def login(self):
        """Log in user, ask for pw,
		compare and if correct set currentUser.
        """
        userName = input('Login: ')
        if self.existUser(userName):
            user = self.getUser(userName)
            rawI = input('Password: ')
            if rawI == user.pw:
                self.currentUser = user
            else: 
                print("Incorrect password!")
                self.login()
        else: 
            print("User do not exist!")
            self.login()
	      

    def logout(self):
        """Log out user, without any kind of check."""
        if self.currentUser is not None:
            self.currentUser = None
            self.run() #For return to login user
        else: print("There is not a login user.")

    def whoAmI(self):
        """Returns what user is current using the shell."""
        print(self.currentUser.name)

    def setAdmin(self, userName, bool):
        """Only for logged in admin user.
		set as admin al already added user.
        """
        if self.currentUser.isAdmin:
            user = self.getUser(userName)
            user.isAdmin = bool
            self.updateUser(userName, user)
        else: print("You are not an admin!")

    def changeCurrentUserPW(self, oldPW, newPW):
        """For normal user.
		change it pw for a new one.
        """
        currentUser = self.getUser(self.currentUser.name)
        if currentUser.pw == oldPW:
            currentUser.pw = newPW
            self.updateUser(currentUser.name, currentUser)
        else: print("Passwords don't match!")

    def changeUserPW(self, userName, newPW):
        """Only for logged in admin user.
		change an user's pw.
        """
        if self.currentUser.isAdmin:
            user = self.getUser(userName)
            user.pw = newPW
            self.updateUser(userName, user)
        else: print("You are not an admin!")

    def existUser(self, userName):
        """Ask if a user is on users dictionary."""
        return userName in self.users.keys()

    def getUser(self, userName):
        """Get a user from users dictionary.
                preCond: -userName must be a string
                         -user must already exists.
        """
        return self.users.get(userName)

    def updateUser(self, userName, user):
        """Update a user's object at the users dictionary."""
        self.users.update({userName: user})

    def run(self):
        """Run while loop for input commands."""
        self.runCommand('login')
        while(True):
            rawI = input('»')
            self.runCommand(rawI)

    def runCommand(self, command):
        """For prompt cut while
               capture commands
        """
        if command in self.validCommands.keys():
            r = self.validCommands.get(command)
            r()
        elif command == '':
            return
        else: print(str(command) + " is not a valid command!")


    def exit(self):
        """Same as logout"""
        self.logout()


class User:

    def __init__(self, userName, userPW, adminBool):
        """Only for creation.
		isAdmin variable must be used only by the shell.
        """
        self.name = userName
        self.pw = userPW
        self.isAdmin = adminBool

    def isAdmin(self):
        return self.isAdmin


admin = User("admin", "adminPW", True)
s = Shell()
s.addAdmin(admin)
s.run()
