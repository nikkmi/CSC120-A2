class ResaleShop:
    #creates resealeShop class which can be used to store computers. In the class, computers can eb added and deleted
    from array import array
    from computer import Computer
    #attributes
    inventory: list=[]

    #constructor
    def __init__(self):
        self.inventory

    #add to inventory
    def buy(self, c: Computer ):
        self.inventory.append(c)
    #clear computer data
    def sell(self, comp:Computer):
        comp.soldComp()
    #print inventory
    def getInventory(self):
        print(" ")
        print("Inventory:")
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

    myOtherComputer: Computer = Computer("2019 MacBook Pro", "Intel", 256, 16, "High Sierra", 2019, 1000)

    myShop.getInventory()
    myShop.buy(myOtherComputer)
    print("Bought Mac Pro 2019")
    myShop.getInventory()
    myShop.sell(myComputer)
    print("Sold 2013 Mac Pro")
    myShop.getInventory() 
    myOtherComputer.newOS("MacOS Monterey")
    print("Updated OS")
    myShop.getInventory() 

if __name__ == "__main__":
    main()