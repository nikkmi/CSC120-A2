class Computer:

    # What attributes will it need?
    #Do I need the ID at all?
    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int 
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,
                    d: str,
                    pro: str,
                    h: int,
                    m: int,
                    o: str,
                    y: int,
                    pri: int ):
        self.description = d
        self.processor_type = pro
        self.hard_drive_capacity = h
        self.memory = m
        self.operating_system = o
        self.year_made = y
        self.price = pri
        
    # What methods will you need?
    '''init - storing information about a specific computer
  - storing the inventory for the store
  newPrice- updating a computer's price
  newOS- updating a computer's OS
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
  actionRefurbish- refurbishing a computer  new_OS
'''
    def newPrice(self, p: int):
        self.price = p
    def newOS(self, OS: str):
        self.operating_system=OS
    def newDes(self, des: str):
        self.description = des
    def newPros(self, p: str):
        self.processor_type = p
    def newHD(self, hd: int):
        self.hard_drive_capacity = hd
    def newMemory(self, m: int):
        self.memory = m
    def newOP(self, op: str): 
        self.operating_system = op
    def newYear(self, y: int):
        self.year = y
    def soldComp(self):
        self.newPrice(0)
        self.newOS("sold")
        self.newDes("sold")
        self.newPros("sold")
        self.newHD("0")
        self.newMemory(0)
        self.newOP("sold")
        self.newYear(0)


    #what is the difference between newOS and refurbich
    def getDes(self):
        return self.description
    def getPros(self):
        return self.processor_type
    def getHD(self):
        return self.hard_drive_capacity
    def getMemory(self):
        return self.memory
    def getOP(self):
        return self.operating_system
    def getYear(self):
        return self.year_made
    def getPrice(self):
        return self.price
        


