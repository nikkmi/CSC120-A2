# Import a few useful containers from the typing module
from typing import Dict, Union

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""


def main():
    
    # First, let's make a computer

    myShop: ResaleShop = new ResaleShop()
    myShop.buy("Mac Pro (Late 2013)", "3.5 GHc 6-Core Intel Xeon E5", 
    1024, 64, "macOS Big Sur", 2013, 1500)

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    myShop.getInventory()

# Calls the main() function when this file is run
#if __name__ == "__main__": main()
