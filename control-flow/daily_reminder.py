task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate customized reminder
match priority:
    case "high":
        if time_bound == "yes":
            reminder = f"🚨 URGENT: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"⚠️ Important: '{task}' is a high priority task that needs your prompt attention."
    case "medium":
        if time_bound == "yes":
            reminder = f"📅 Scheduled: '{task}' is a medium priority task due soon - please schedule time for it."
        else:
            reminder = f"📝 Note: '{task}' is a medium priority task to address when convenient."
    case "low":
        if time_bound == "yes":
            reminder = f"⏳ Flexible: '{task}' is a low priority task with an upcoming but flexible deadline."
        else:
            reminder = f"🌱 Whenever: '{task}' is a low priority task to consider when you have free time."
    case _:
        reminder = "❌ Error: Invalid priority level. Please use high, medium, or low."

# Print the final reminder
print("\n" + reminder)