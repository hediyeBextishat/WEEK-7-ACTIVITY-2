# 1. Factory Pattern: Handles creating fish
class FishFactory:   
    @staticmethod
    def create_fish(name):
        return {"name": name.capitalize()}

# 2. Singleton Pattern：ensures that no matter how many times you try to create an "Aquarium," you only ever get one instance. This prevents data loss.
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
     #This is the logic that processes your inputs.
     #self.inventory.get(fish["name"], 0): This is a safe way to check the dictionary. 
     
    def show(self):
        print("\n--- Aquarium Inventory ---")
        for fish, count in self.inventory.items():
            print(f"{fish}: {count}")
            # If the fish is already in there, it returns the number; if not, it returns 0 so we don't get an error.

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
