import os
from datetime import datetime

def get_folder_size(folder_path):

    total_size = 0

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)

            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)

    return total_size


def format_size(size_bytes):

    gb = size_bytes / (1024**3)
    mb = size_bytes / (1024**2)

    if gb >= 1:
        return f"{gb:.2f} GB"
    else:
        return f"{mb:.2f} MB"


def analyze_directory(path):

    folders = []

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):

            size = get_folder_size(full_path)

            folders.append((item, size))

    folders.sort(key=lambda x: x[1], reverse=True)

    print("\n===== DISK USAGE ANALYSIS =====\n")

    report_lines = []

    for name, size in folders:

        size_formatted = format_size(size)

        line = f"{name} : {size_formatted}"

        print(line)

        report_lines.append(line)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    report_name = f"disk_report_{timestamp}.txt"

    with open(report_name, "w") as report:

        report.write("===== DISK USAGE REPORT =====\n\n")

        for line in report_lines:
            report.write(line + "\n")

    print(f"\nReport saved as {report_name}")


print("\nDISK USAGE ANALYZER")
print("-" * 30)

directory = input("Enter directory path: ").strip('"')

if not os.path.exists(directory):
    print("Directory not found.")
else:
    analyze_directory(directory)
