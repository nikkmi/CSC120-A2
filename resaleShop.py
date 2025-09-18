class ResaleShop:

    from array import array
    # What attributes will it need?
    inventory = array.array
    condition
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__():
        self.inventory

    # What methods will you need?
    ''' - storing the inventory for the store
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
   '''
    def add_invetrory(self, comp: Computer):
        self.inventory.append(comp)


    def buy(self, d: str,
                    pro: str,
                    h: int,
                    m: int,
                    o: str,
                    y: int,
                    pri: int ):
    #construct computer, append
        newComputer: Computer = Computer(d: str,
                    pro: str,
                    h: int,
                    m: int,
                    o: str,
                    y: int,
                    pri: int)
        inventoryAppend(newComputer)

    def sell(self, comp:Computer):
        int n = self.inventory.index(comp)
        self.inventory.remove(n)
        self.inventory.insert(n, "Sold")

    def getInventory():
        print(inventory)

