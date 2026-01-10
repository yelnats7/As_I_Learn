import datetime

def main():
    try:
        user_input = input("Enter your goal and the date (Goal:dd/mm/yyyy):\n").split(":")
        
        goal = user_input[0]
        deadline = user_input[1].strip()

        deadline_date = datetime.datetime.strptime(deadline, "%d/%m/%Y")
        current_date = datetime.datetime.now()

        days_left = (deadline_date - current_date).days
        print(f"You have {days_left} days left to achieve: {goal}")

    except IndexError:
        print("Error: You forgot to separate the goal and date with a colon (:).")
    except ValueError:
        print("Error: The date format should be Day/Month/Year (e.g., 31/12/2025).")

main()
