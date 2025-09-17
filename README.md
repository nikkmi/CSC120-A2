# CSC120-A2: Object-ification

This repository contains starter code for A2: Object-ification, developed for CSC120: Object-Oriented Programming as taught by Prof. R. Jordan Crouser and Prof. Ab Mosca at Smith College in Spring 2025.
  
 `procedural_resale_shop.py` contains a procedural program to perform the basic functions of a computer resale store:
   - buying a computer (add to inventory)
   - selling a computer (remove from inventory)
   - updating the price of an item in the inventory
   - printing the inventory
   - refurbishing a computer (update price based on age of machine, optionally update OS)
   
  `main.py` contains a simple demonstration of each of these functions, plus a helper function to create a "computer"
  
  ## Your task
  
  **Step 1**: Fork this repository so you (and your partners, if applicable) have your own copy of this code.
  
  **Step 2**: Fill in the class definitions in `computer.py` and `oo_resale_shop.py` with the appropriate functionality from the provided procedural code, re-written using Object-Oriented Programming techniques. Consider carefully which classes should be responsible for which behaviors / information:
  - storing information about a specific computer
  - storing the inventory for the store
  - updating a computer's price
  - updating a computer's OS
  - buying a computer (add to inventory)
  - selling a computer (remove from inventory)
  - refurbishing a computer

 **Step 3**: Be sure to test your code! The items contained in `rubric.md` are a useful guide.
 
**Step 4**: Fill in `rubric.md` wth your self-assessment and include your reflection on the assignment in `reflection.md`, then submit your repo to Gradescope.

Notes:"""# Now, let's refurbish it
    "new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")""""
    """
    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")
"""
"""computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )"""
"""def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }"""