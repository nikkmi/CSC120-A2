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
    #what is the difference between newOS and refurbich
    def actionRefurbish(self, OS: str):
        self.operating_system = OS

from resale_shop import ResaleShop

def main():
    myShop: ResaleShop = ResaleShop()
    myShop.buy("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 
    1024, 64, "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    myShop.getInventory()

if __name__ == "__main__":
    main()