task = input("Enter the task description.") 
priority = input("Set the tasks priotity(high, medium, low): ").lower()
time_bound = input("Is the task time bound? (yes or no): ").lower()
match priority:
    case "high":
        reminder= f"{task} is HIGH priority."
    case "medium":
        reminder= f"{task} is MEDIUM priority."
    case "low":
        reminder= f"{task} is LOW priority. "
    case _:
        reminder= "Invalid priority entered."
if time_bound== "yes":
    reminder= "This requires immmediate attention."
print(reminder)