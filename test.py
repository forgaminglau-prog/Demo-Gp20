import requests
import json

BASE_URL = "https://cloud-demo-group-20.onrender.com/api/items"

def create_item():
    name = input("Enter item name: ").strip()
    quantity_input = input("Enter item quantity: ").strip()

    if not name or not quantity_input:
        print("Error: Name and quantity cannot be empty.")
        return

    try:
        quantity = int(quantity_input)
    except ValueError:
        print("Error: Quantity must be a number.")
        return

    payload = {"name": name, "quantity": quantity}

    print("\nEquivalent cURL command:")
    print(f"""curl -X POST {BASE_URL} \\
-H "Content-Type: application/json" \\
-d '{{"name":"{name}" ,"quantity":{quantity}}}'""")

    response = requests.post(BASE_URL, json=payload)

    if response.status_code == 201:
        print("Item created successfully.")
        print(response.json())
    else:
        print(f"Failed to create item. Status: {response.status_code}")
        print(response.text)

def read_items():
    print("\nEquivalent cURL command:")
    print(f"curl {BASE_URL}")

    response = requests.get(BASE_URL)
    if response.status_code == 200:
        print("All Items:")
        items = response.json()
        for item in items:
            print(f"- ID: {item['_id']} , Name: {item['name']} , Quantity: {item['quantity']}")
    else:
        print(f"Failed to fetch items. Status: {response.status_code}")
        print(response.text)

def update_item():
    item_id = input("Enter the ID of the item to update: ").strip()
    if not item_id:
        print("Error: ID cannot be empty.")
        return

    # Fetch current item to preserve unchanged fields
    current = requests.get(f"{BASE_URL}/{item_id}")
    if current.status_code != 200:
        print("Error: Item not found or cannot fetch current data.")
        return
    existing = current.json()
    name = existing.get("name", "")
    quantity = existing.get("quantity", 0)

    print("\nWhat would you like to update?")
    print("1 Name only")
    print("2 Quantity only")
    print("3 Both name and quantity")
    choice = input("Enter your choice (1-3): ").strip()

    if choice == "1":
        new_name = input("Enter the new name: ").strip()
        if not new_name:
            print("Error: Name cannot be empty.")
            return
        name = new_name
    elif choice == "2":
        new_quantity_input = input("Enter the new quantity: ").strip()
        try:
            quantity = int(new_quantity_input)
        except ValueError:
            print("Error: Quantity must be a number.")
            return
    elif choice == "3":
        new_name = input("Enter the new name: ").strip()
        new_quantity_input = input("Enter the new quantity: ").strip()
        if not new_name or not new_quantity_input:
            print("Error: Name and quantity cannot be empty.")
            return
        try:
            name = new_name
            quantity = int(new_quantity_input)
        except ValueError:
            print("Error: Quantity must be a number.")
            return
    else:
        print("Invalid choice. Update cancelled.")
        return

    payload = {"name": name, "quantity": quantity}

    print("\nEquivalent cURL command:")
    print(f"""curl -X PUT {BASE_URL}/{item_id} \\
-H "Content-Type: application/json" \\
-d '{json.dumps(payload)}'""")

    response = requests.put(f"{BASE_URL}/{item_id}", json=payload)
    if response.status_code == 200:
        print("Item updated successfully.")
        print(response.json())
    elif response.status_code == 404:
        print("Error: Item not found.")
    else:
        print(f"Failed to update item. Status: {response.status_code}")
        print(response.text)

def delete_item():
    item_id = input("Enter the ID of the item to delete: ").strip()
    if not item_id:
        print("Error: ID cannot be empty.")
        return

    print("\nEquivalent cURL command:")
    print(f"curl -X DELETE {BASE_URL}/{item_id}")

    response = requests.delete(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("Item deleted successfully.")
        print(response.json())
    elif response.status_code == 404:
        print("Error: Item not found.")
    else:
        print(f"Failed to delete item. Status: {response.status_code}")
        print(response.text)

def search_item():
    item_id = input("\nEnter item ID to search: ").strip()
    if not item_id:
        print("Error: ID cannot be empty.")
        return

    print("\nEquivalent cURL command:")
    print(f"curl {BASE_URL}/{item_id}")

    response = requests.get(f"{BASE_URL}/{item_id}")
    if response.status_code == 200:
        print("Item found:")
        print(response.json())
    elif response.status_code == 404:
        print("Item not found.")
    else:
        print(f"Failed to search. Status: {response.status_code}")
        print(response.text)

def main():
    while True:
        print("\nCloud CRUD API Tester")
        print("1 Create a new item")
        print("2 Read all items")
        print("3 Update an item")
        print("4 Delete an item")
        print("5 Search item by ID")
        print("0 Exit")
        choice = input("Enter your choice (0-5): ").strip()

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
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 0 to 5.")

if __name__ == "__main__":
    main()
