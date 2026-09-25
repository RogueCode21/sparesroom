import inventory
import database 

def add_part_flow() :
        name = input("Part name: ")
        category = input("Category (Mechanical/Electrical/Pneumatics/Tooling/Fasterners): ")
        
        try:
            qty = int(input("Intial quantity: "))
            reorder_point = int(input("Reorder point: "))
        except ValueError:
            print("Quatity and reoder point must be numbers")
            return
        
        description = input("Description: ")

        inventory.add_part(name, category,qty, reorder_point, description)
        print(f"Added {name}")

def adjust_quantity_flow():
    try: 
        part_id = int(input("Part ID: "))
        change = int(input(" Amount (positive to increase, negative to decrease): "))
    except ValueError: 
        print("Part ID and amount must be numbers.")
        return

    success = inventory.adjust_quantity(part_id, change)
    if not success:
        print("Part not found.")

while True: 
    command = input("\nCommand (add / adjust / quit): ").strip().lower()
    if command == "add":
        add_part_flow()
    elif command == "adjust": 
        adjust_quantity_flow()
    elif command == "quit":
        break
    else:
        print("Unknown command.")

        