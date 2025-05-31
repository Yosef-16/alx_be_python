task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority and time sensitivity
match priority:
    case "high":
        if time_bound == "yes":
            message = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            message = f"Reminder: '{task}' is a high priority task. Please address it soon."
    case "medium":
        if time_bound == "yes":
            message = f"Note: '{task}' is a medium priority task that should be completed this week."
        else:
            message = f"Note: '{task}' is a medium priority task. Consider completing it when possible."
    case "low":
        if time_bound == "yes":
            message = f"Note: '{task}' is a low priority task with a flexible deadline."
        else:
            message = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        message = "Invalid priority level entered. Please use high, medium, or low."

# Print the final message
print("\n" + message)