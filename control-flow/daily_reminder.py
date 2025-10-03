def main():
    task = input("Enter your task: ").strip()
    priority = input("Priority (high/medium/low): ").strip().lower()
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' has an unspecified priority"

    if time_bound == "yes" and priority in ["high", "medium", "low"]:
        message += " that requires immediate attention today!"
    elif time_bound == "no" and priority in ["high", "medium", "low"]:
        message += ". Consider completing it when you have free time."
    else:
        message += "."

    print(f"Reminder: {message}")

if __name__ == "__main__":
    main()