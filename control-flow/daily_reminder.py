task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task and create reminder message
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Handle priority and time sensitivity
match priority:
    case "high":
        reminder += " that requires immediate attention"
    case "medium":
        reminder += " that should be addressed soon"
    case "low":
        reminder += " that can be done when convenient"
    case _:
        reminder = "Invalid priority level entered"

# Add time-bound urgency if applicable
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " today!"
elif priority in ["high", "medium", "low"]:
    reminder += "."

# Print the final reminder
print("\n" + reminder)