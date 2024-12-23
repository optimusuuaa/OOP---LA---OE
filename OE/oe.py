class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}"

    def update_price(self, new_price):
        self.price = new_price

    def modify_phone_properties(self, new_brand=None, new_model=None, new_price=None):
        if new_brand:
            self.brand = new_brand
        if new_model:
            self.model = new_model
        if new_price:
            self.update_price(new_price)

    def delete_properties(self):
        self.brand = None
        self.model = None
        self.price = None

    def delete_phone(self):
        del self

def menu():
    phones = []
    while True:
        print("\nMain Menu:")
        print("1. Add Phone")
        print("2. Modify Phone")
        print("3. Delete Phone")
        print("4. Display Phones")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = float(input("Enter price: "))
            phones.append(Phone(brand, model, price))

        elif choice == '2':
            index = int(input("Enter index of phone to modify: "))
            if 0 <= index < len(phones):
                new_brand = input("Enter new brand (leave blank if no change): ")
                new_model = input("Enter new model (leave blank if no change): ")
                new_price = input("Enter new price (leave blank if no change): ")
                new_price = float(new_price) if new_price else None
                phones[index].modify_phone_properties(new_brand, new_model, new_price)
            else:
                print("Invalid index!")

        elif choice == '3':
            index = int(input("Enter index of phone to delete: "))
            if 0 <= index < len(phones):
                phones.pop(index)
                print("Phone deleted successfully!")
            else:
                print("Invalid index!")

        elif choice == '4':
            if phones:
                for idx, phone in enumerate(phones):
                    print(f"[{idx}] {phone}")
            else:
                print("No phones available.")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    menu()
