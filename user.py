# Define the Profile class
class Profile:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.friends = []

    def setUsername(self, newUser):
        self.username = newUser

    def setName(self, newName):
        self.name = newName

    def setEmail(self, newEmail):
        self.email = newEmail

    def getUsername(self):
        return self.username

    def addFriend(self, person):
        "Add a person to this Person's friends"
        if person is not self:
            self.friends.append(person)

    def getNumFriends(self):
        "Returns how many friends this Person has"
        return len(self.friends)

    def getFriends(self):
        """Returns a list of Person objects that are friends with this
        Person."""
        return self.friends
    
