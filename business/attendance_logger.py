from datetime import datetime

print("EMPLOYEE ATTENDANCE LOGGER")
print("-" * 30)
print("Type 'exit' to close.\n")

file_name = "attendance_log.txt"

while True:

    employee_name = input("Enter employee name: ").strip()

    if employee_name.lower() == "exit":
        print("\nProgram closed.")
        break

    if employee_name == "":
        print("Invalid name.\n")
        continue

    now = datetime.now()

    date_today = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{date_today} | {employee_name} | Check-in | {time_now}\n")

    print("Attendance registered successfully.\n")