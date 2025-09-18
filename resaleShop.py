class ResaleShop:

    from array import array
    from computer import Computer
    # What attributes will it need?
    inventory: list=[]

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory

    # What methods will you need?
    ''' - storing the inventory for the store
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
   '''

    def buy(self, c: Computer ):
    #append
        self.inventory.append(c)

    def sell(self, comp:Computer):
        comp.soldComp()

    def getInventory(self):
        for x in self.inventory:
            if x.getPrice() != 0:
                print(x.getPros())
                print(x.getDes())
                print(x.getHD())
                print(x.getMemory())
                print(x.getOP())
                print(x.getYear())
                print(x.getPrice())
                print("*"*21)

#do I need the random print statements like in the main 

def main():
    from computer import Computer
    myShop: ResaleShop = ResaleShop ()
    myComputer: Computer = Computer("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 1024, 64, "macOS Big Sur", 2013, 1500)
    myShop.buy(myComputer)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    myShop.getInventory()
    myShop.sell(myComputer)
    myShop.getInventory()
    
    #new os, new_OS = "MacOS Monterey"
    '''"Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500'''

#is it okay if I don't actualy delete stuff from the inventory?
#error messages????
#comments
#naming conventions
if __name__ == "__main__":
    main()