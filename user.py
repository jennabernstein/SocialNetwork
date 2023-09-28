
# Define the Profile class
class Profile:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.friends = []

    def setUsername(self, newUser):
        "Set the username of the Person"
        self.username = newUser

    def setName(self, newName):
        "Set the name of the Person"
        self.name = newName

    def setEmail(self, newEmail):
        "Set the email of the Person"
        self.email = newEmail

    def getUsername(self):
        "Return the username of the Person"
        return self.username

    def getNumFriends(self):
        "Returns how many friends this Person has"
        return len(self.friends)

    def getFriends(self):
        """Returns a list of Person objects that are friends with this
        Person."""
        return self.friends
    
