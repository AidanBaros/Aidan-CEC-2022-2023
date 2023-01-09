class Student:
    def __init__(self, name, ID, Color, next=None):
        self.name = name
        self.ID = ID
        self.next = next
        self.Color = Color


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, name, ID, Color):
        newStudent = Student(name, ID, Color)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newStudent
        else:
            self.head = newStudent
    
    def printList(self):
        current = self.head
        while current:
            print(f"Student name: {current.name}, ID: {current.ID}, Favorite Color: {current.Color}")
            current = current.next
    
StudentLine = LinkedList()

StudentLine.insert("Lily", 456987, "Beige")
StudentLine.insert("Kevin", 123987, "Cinnamon")
StudentLine.insert("Sebastian", 4, "Crewmate Red")
StudentLine.insert("Kyle", 756937, "Gold")
StudentLine.insert("Cory", 783469, "Eigengrau")
StudentLine.insert("Bob", 234589, "Navy Blue")

StudentLine.printList()