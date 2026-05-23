# 1. Factory Pattern: Handles creating fish
class FishFactory:   
    @staticmethod
    def create_fish(name):
        return {"name": name.capitalize()}

# 2. Singleton Pattern: Ensures only one aquarium exists
class Aquarium:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.inventory = {}
        return cls._instance

    def add_fish(self, name, qty):
        fish = FishFactory.create_fish(name)
        self.inventory[fish["name"]] = self.inventory.get(fish["name"], 0) + qty

    def show(self):
        print("\n--- Aquarium Inventory ---")
        for fish, count in self.inventory.items():
            print(f"{fish}: {count}")

# 3. Running the program
if __name__ == "__main__":
    tank = Aquarium()
    print("Type 'exit' to stop.")
    
    while True:
        name = input("\nFish type: ")
        if name.lower() == 'exit': break
        try:
            qty = int(input("Quantity: "))
            tank.add_fish(name, qty)
            tank.show()
        except:
            print("Invalid input.")