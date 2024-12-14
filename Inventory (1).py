class Product:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.product_description}, Price: {self.price}, Quantity: {self.quantity}"

class InventoryManagementSystem:
    def __init__(self):
        self.products = []

    def add_product(self, product_id, name, product_description, price, quantity):
        new_product = Product(product_id, name, product_description, price, quantity)
        self.products.append(new_product)
        print(f"Product '{name}' added successfully.")

    def update_stock(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.quantity += quantity
                print(f"Stock updated for '{product.name}'. New quantity: {product.quantity}")
                return
        print("Product not found.")

    def display_products(self):
        if not self.products:
            print("No products in inventory.")
            return
        for product in self.products:
            print(product)

    def calculate_total_value(self):
        total_value = sum(product.price * product.quantity for product in self.products)
        print(f"Total value of inventory: {total_value}")

def main():
    inventory_system = InventoryManagementSystem()

    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Stock Quantity")
        print("3. View All Products")
        print("4. Calculate Total Value of Inventory")
        print("5. Exit")
        
        choice = input("Select an action (1-5): ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory_system.add_product(product_id, name, product_description, price, quantity)

        elif choice == '2':
            product_id = input("Enter product ID to update: ")
            quantity = int(input("Enter quantity to add (use negative number to decrease): "))
            inventory_system.update_stock(product_id, quantity)

        elif choice == '3':
            inventory_system.display_products()

        elif choice == '4':
            inventory_system.calculate_total_value()

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()