class ResaleShop:

    from array import array
    from computer import Computer
    # What attributes will it need?
    inventory: list=[]
    name: str
  



    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, n:str):
        self.name = n
        self.inventory

    # What methods will you need?
    ''' - storing the inventory for the store
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
   '''
    def add_invetrory(self, comp: Computer):
        self.inventory.append(comp)


    def buy(d: str,
                    pro: str,
                    h: int,
                    m: int,
                    o: str,
                    y: int,
                    pri: int ):
    #construct computer, append
        newComputer: Computer = self.Computer( d, pro, h, m, o, y, pri)
        inventoryAppend(newComputer)

    def sell(self, comp:Computer):
        self.n = self.inventory.index(comp)
        self.inventory.remove(self, n)
        self.inventory.insert(self, n, "Sold")

    def getInventory(self):
        print(inventory)

def main():
    myShop: ResaleShop = ResaleShop ("Smith Computer Shop")
    myShop.buy("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 
    1024, 64, "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    myShop.getInventory()

if __name__ == "__main__":
    main()