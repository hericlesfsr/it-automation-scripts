import os

log_file = input("Enter the log file path: ").strip('"')

print("\nLOG ANALYZER TOOL")
print("-" * 25)

errors = 0
warnings = 0
failed_logins = 0

# Check if file exists
if not os.path.exists(log_file):
    print("Error: File not found.")
    exit()

with open(log_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.lower()

        if "error" in line:
            errors += 1

        if "warning" in line:
            warnings += 1

        if "login failed" in line:
            failed_logins += 1

report = f"""
===== LOG ANALYSIS REPORT =====

Errors found: {errors}
Warnings found: {warnings}
Failed logins: {failed_logins}
"""

print(report)

with open("log_report.txt", "w") as report_file:
    report_file.write(report)

print("Report saved as log_report.txt")