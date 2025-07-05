task = input("Enter the task description.") 
priority = input("Set the tasks priotity(high, medium, low): ").lower()
time_bound = input("Is the task time bound? (yes or no): ").lower()
match time_bound:
    case "yes":
        print(f"Reminder: Finish project report")   
    case "no":
        print("Note:'Read a book' is a low priority task")