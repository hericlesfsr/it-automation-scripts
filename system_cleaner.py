import os
import shutil
import platform

def clean_system_files():
    # Windows standard temporary directory environment variables
    temp_paths = [
        os.environ.get('TEMP'),                             # User Temporary files
        os.path.join(os.environ.get('SystemRoot'), 'Temp'), # System-wide Temp files
        os.path.join(os.environ.get('LocalAppdata'), 'Temp') # Local App Cache
    ]

    print("--- 🧹 System Cleanup Initiated ---")
    items_removed = 0
    items_skipped = 0

    for path in temp_paths:
        if path and os.path.exists(path):
            print(f"\nScanning directory: {path}")
            
            try:
                # Attempt to list files in the directory
                directory_contents = os.listdir(path)
            except PermissionError:
                print(f"[⚠️] ACCESS DENIED: Please run as Administrator to clean this folder.")
                continue 

            for item in directory_contents:
                item_full_path = os.path.join(path, item)
                try:
                    # Check if it's a file or a symbolic link
                    if os.path.isfile(item_full_path) or os.path.islink(item_full_path):
                        os.unlink(item_full_path) 
                        items_removed += 1
                        print(f"[✅] Removed: {item}")
                    
                    # Check if it's a directory
                    elif os.path.isdir(item_full_path):
                        shutil.rmtree(item_full_path)
                        items_removed += 1
                        print(f"[✅] Folder Deleted: {item}")
                
                except Exception:
                    # Files currently in use by the OS or other apps cannot be deleted
                    print(f"[❌] Busy/In Use: {item}")
                    items_skipped += 1

    print("\n" + "="*40)
    print(f"CLEANUP SUMMARY:")
    print(f"✨ Total items removed: {items_removed}")
    print(f"🔒 Items kept (Active/Busy): {items_skipped}")
    print("="*40)

if __name__ == "__main__":
    if platform.system() == "Windows":
        clean_system_files()
    else:
        print("Error: This automation is designed for Windows environments.")
        