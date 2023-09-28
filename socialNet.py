from user import Profile

class SocialNetwork:

    """Represents a social network, containing ids that map to Person
    objects.  Contains functionality for manipulating a social
    network.

    """

    def __init__(self):
        "Creates a new, empty social network"
        self._useridToPerson = {}

    def __str__(self):
        "Returns a string representing the social network"
        rep = ""

        userids = self.getUserIDs()
        userids.sort()
        
        for userid in userids:
            rep += str(self._useridToPerson[userid]) + "\n"
        return rep


    def getPeople(self):
        """Returns the list of Persons in the social network"""
        return list(self._useridToPerson.values())
    
    def getNonFriends(self, person):
        """Returns a list of all Person objects that this Person is not friends with."""
        nonfriends = []
        for user in self._useridToPerson.values():
            if user not in person.getFriends() and user is not person:
                nonfriends.append(user)
        return nonfriends
        
        
    def getUserIDs(self):
        """ Return the list of user ids in the social network """
        return list(self._useridToPerson.keys())
        
        
    def hasUserID(self, userid):
        """Returns True iff this userid already exists in the SocialNetwork.
        Parameter:
            userid - a string that represents a Person's id
        """
        return (userid in self._useridToPerson)

        
    def getPerson(self, userid):
        """Returns the Person object with the given userid or None if no
        person has that userid.
        Parameter:
            userid - a string representing a Person's id"""
        return self._useridToPerson.get(userid)

    def addPerson(self, person):
        self._useridToPerson[person.getUsername()] = person

    def addPeople(self, people):
        for person in people:
            self._useridToPerson[person.getUsername()] = person

    def addFriends(self, person1, person2):
        "Add a person to each person's friend list"
        if person1 is not person2:
            person1.friends.append(person2)
            person2.friends.append(person1)

    def addFriendList(self, person, people):
        "Add a list of people to this Person's friends"
        for user in people:
            self.addFriends(person, user)