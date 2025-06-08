def display_menu():
    print("Shopping List Menu:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View shopping list")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")
    else:
        print("Item cannot be empty.")

def remove_item(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty. Nothing to remove.")
        return
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' is not in your shopping list.")

def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        print("Your shopping list:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the program. Happy shopping!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")

if __name__ == "__main__":
    main()