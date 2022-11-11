import random
import winsound


class Train:
    def __init__(self, Type, next=None):
        self.Type = Type
        self.ID = random.randint(100, 999)
        self.isFull = False
        self.next = next
        if self.Type.lower() == "locomotive":
            self.hornDuration = 2000
            self.hornFrequency = 500

    def honk(self):
        winsound.Beep(self.hornFrequency,self.hornDuration)


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, Type):
        newTrain = Train(Type)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = newTrain
        else:
            self.head = newTrain

    def printList(self):
        current = self.head
        yesNo = "No"
        if current.isFull == False:
            yesNo = "No"
        else:
            yesNo = "Yes"
        while current:
            print(
                f"Train car type: {current.Type}, Train car ID: {current.ID}, Train car full: {yesNo}"
            )
            current = current.next
        print()

    def searchID(self, ID):
        current = self.head
        while current:
            if current.ID == ID:
                print(f"Car ID {ID} is a {current.Type} car\n")
            current = current.next
        
    def searchCargo(self, type):
        current = self.head
        Num = 0
        types = ""
        if type == 1:
            types = "locomotive"
        if type == 2:
            types = "coal"
        if type == 3:
            types = "oil"
        if type == 4:
            types = "automobile"
        if type == 5:
            types = "shipping"
        while current:
            if current.Type == types:
                Num += 1
            current = current.next
        print(f"There are {Num} {types} cars in the train\n")

    def Honk(self):
        current = self.head
        while current:
            if current.Type == "locomotive":
                current.honk()
            current = current.next
    
    
lists = LinkedList()

while True:
    inp = input(
        "Would you like to: \n1. Add cars to the train \n2. Print a list of the train cars out \n3. Search the train by ID \n4. Search for cargo\n5. Honk the horns\n\n Enter the corisponding number\n -- "
    )
    if inp == "1":
        inp1 = input(
            "What type of car would you like to add: \n1. locomotive\n2. coal\n3. oil\n4. automobile\n5. shipping\n -- "
        )
        if inp1 == "1":
            lists.insert("locomotive")
        elif inp1 == "2":
            lists.insert("coal")
        elif inp1 == "3":
            lists.insert("oil")
        elif inp1 == "4":
            lists.insert("automobile")
        elif inp1 == "5":
            lists.insert("shipping")
        else:
            print("error")
        
    elif inp == "2":
        lists.printList()
    elif inp == "3":
        inp3 = int(input(
            "What is the ID you want to find\n -- "
        ))
        lists.searchID(inp3)
    elif inp == "4":
        inp4 = int(input(
            "What type of cargo are you looking for \n1. locomotive\n2. coal\n3. oil\n4. automobile\n5. shipping\n -- "
        ))
        lists.searchCargo(inp4)
    elif inp == "5":
        lists.Honk()
    else:
        pass
