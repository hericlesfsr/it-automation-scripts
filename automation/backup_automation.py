import os
import shutil
from datetime import datetime

print("AUTOMATED FILE BACKUP TOOL")
print("-" * 30)

source_folder = input("Enter source folder path: ").strip('"')
backup_destination = input("Enter backup destination path: ").strip('"')

if not os.path.exists(source_folder):
    print("Source folder not found.")
    exit()

if not os.path.exists(backup_destination):
    print("Backup destination not found.")
    exit()

folder_name = os.path.basename(source_folder)

date_now = datetime.now().strftime("%Y%m%d_%H%M%S")

new_backup_folder = folder_name + "_backup_" + date_now

final_path = os.path.join(backup_destination, new_backup_folder)

try:
    shutil.copytree(source_folder, final_path)

    print("\nBackup completed successfully.")
    print("Backup created in:")
    print(final_path)

except Exception as error:
    print("Error during backup:")
    print(error)