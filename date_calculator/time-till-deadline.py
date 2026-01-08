from datetime import datetime, date

def main():
    goal = input("Enter your goal with a deadline sepaarated by a colon\n")
    deadline = goal.split(":")

    deadline_date = deadline[1]
    current_date = str(date.today().strftime("%d/%m/%Y"))

    dates = [deadline_date, current_date]

    #format_code = "%d/%m/%Y"
    #deadline_date_object = datetime.strptime(deadline_date, format_code)
    datees = {"date1": None, "date2": None}
    key_list =["date1", "date2"]

    def format_date(date_given):
        return date(int(date_given.split("/")[2]), int(date_given.split("/")[1]), int(date_given.split("/")[0]))
    for i in range(2):
        current_key = key_list[i]
        datees[current_key] = format_date(dates[i])

    print(f"{(datees["date1"] - datees["date2"]).days} days")
main()
