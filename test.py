import requests

BASE_URL = "https://cloud-demo-group-20.onrender.com/api/items"

def create_item():
    name = input("Enter item name: ").strip()
    quantity_input = input("Enter item quantity: ").strip()

    if not name or not quantity_input:
        print(" Error: Name and quantity cannot be empty.")
        return

    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Error: Quantity must be a number.")
        return

    payload = {"name": name, "quantity": quantity}
    response = requests.post(BASE_URL, json=payload)

    if response.status_code == 201:
        print("Item created successfully.")
        print(response.json())
    else:
        print(f"Failed to create item. Status: {response.status_code}")
        print(response.text)

def read_items():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("All Items:")
        items = response.json()
        for item in items:
            print(f"- ID: {item['_id']}, Name: {item['name']}, Quantity: {item['quantity']}")
    else:
        print(f"Failed to fetch items. Status: {response.status_code}")
        print(response.text)

def update_item():
    item_id = input("Enter the ID of the item to update: ").strip()
    if not item_id:
        print("Error: ID cannot be empty.")
        return

    print("\nWhat would you like to update?")
    print("1 Name only")
    print("2 Quantity only")
    print("3 Both name and quantity")
    choice = input("Enter your choice (1-3): ")

    payload = {}
    if choice == "1":
        new_name = input("Enter the new name: ").strip()
        if not new_name:
            print(" Error: Name cannot be empty.")
            return
        payload["name"] = new_name
    elif choice == "2":
        new_quantity_input = input("Enter the new quantity: ").strip()
        try:
            payload["quantity"] = int(new_quantity_input)
        except ValueError:
            print(" Error: Quantity must be a number.")
            return
    elif choice == "3":
        new_name = input("Enter the new name: ").strip()
        new_quantity_input = input("Enter the new quantity: ").strip()
        if not new_name or not new_quantity_input:
            print(" Error: Name and quantity cannot be empty.")
            return
        try:
            payload = {"name": new_name, "quantity": int(new_quantity_input)}
        except ValueError:
            print(" Error: Quantity must be a number.")
            return
    else:
        print(" Invalid choice. Update cancelled.")
        return

    response = requests.put(f"{BASE_URL}/{item_id}", json=payload)
    if response.status_code == 200:
        print(" Item updated successfully.")
        print(response.json())
    elif response.status_code == 404:
        print(" Error: Item not found.")
    else:
        print(f"❌ Failed to update item. Status: {response.status_code}")
        print(response.text)

def delete_item():
    item_id = input("Enter the ID of the item to delete: ").strip()
    if not item_id:
        print(" Error: ID cannot be empty.")
        return

    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print(" Item deleted successfully.")
        print(response.json())
    elif response.status_code == 404:
        print(" Error: Item not found.")
    else:
        print(f" Failed to delete item. Status: {response.status_code}")
        print(response.text)

def search_item():
    print("\n Search by:")
    print("1 ID")
    print("2 Name")
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        item_id = input("Enter item ID: ").strip()
        if not item_id:
            print(" Error: ID cannot be empty.")
            return
        response = requests.get(f"{BASE_URL}/{item_id}")
        if response.status_code == 200:
            print(" Item found:")
            print(response.json())
        elif response.status_code == 404:
            print(" Item not found.")
        else:
            print(f" Failed to search. Status: {response.status_code}")
            print(response.text)

    elif choice == "2":
        name = input("Enter item name: ").strip()
        if not name:
            print("Error: Name cannot be empty.")
            return
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            items = response.json()
            matches = [item for item in items if item["name"].lower() == name.lower()]
            if matches:
                print(f"Found {len(matches)} item(s):")
                for item in matches:
                    print(f"- ID: {item['_id']}, Name: {item['name']}, Quantity: {item['quantity']}")
            else:
                print("No item found with that name.")
        else:
            print(f" Failed to search. Status: {response.status_code}")
            print(response.text)
    else:
        print("Invalid choice.")

def main():
    print("\n Cloud CRUD API Tester")
    print("1 Create a new item")
    print("2 Read all items")
    print("3 Update an item")
    print("4 Delete an item")
    print("5 Search item by ID or name")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        create_item()
    elif choice == "2":
        read_items()
    elif choice == "3":
        update_item()
    elif choice == "4":
        delete_item()
    elif choice == "5":
        search_item()
    else:
        print(" Invalid option. Please enter 1 to 5.")

if __name__ == "__main__":
    main()

