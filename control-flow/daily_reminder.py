task=input("Enter your task: ")
priority=input("Priority (high/medium/low): ")
time_bound=input("Is it time-bound? (yes/no): ")

while priority not in ["high", "medium", "low"]:
    print("Please enter a valid priority: high, medium, or low.")
    priority=input("Priority (high/medium/low): ")

match priority:
    case "high":
        reminder=f"'{task}' is a high priority task"
    case "medium":
        reminder=f"'{task}' is a medium priority task"
    case "low":
        reminder=f"'{task}' is a low priority task"
    case _:
        reminder=f"'{task}' has an unspecified priority"

if time_bound=="yes":
    reminder+= " that requires immediate attention today!"
    
else:
    reminder=f"Note: {reminder}. Consider completing it when you have free time."
    print("Reminder: ", reminder)
