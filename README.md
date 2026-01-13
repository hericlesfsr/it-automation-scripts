# IT Automation Scripts for IT Support

📋 **Description**

This repository contains a collection of Python automation scripts designed to assist IT Support and Infrastructure teams with common operational tasks such as system health checks, system information reporting, and file organization. 
The tools are lightweight, portable, and focused on improving troubleshooting efficiency and operational productivity.

🚀 **Available Tools**

🔹 **Currency & Market Monitor**
A real-time financial monitoring tool that connects to external APIs to fetch currency exchange rates.
* **Features:**
    * Real-time data for USD, EUR, and BTC.
    * Integration with REST APIs (JSON handling).
    * Automatic history logging in .txt format.
    * One-click execution via .bat file.
* **Files:** `currency_monitor.py`, `run_monitor.bat`.

🔹 **System Health Check**
A portable diagnostic tool developed in Python to perform quick system health checks.
* **Features:**
    * Checks available disk space.
    * Verifies internet connectivity.
    * Designed for fast troubleshooting.
    * Portable execution via .bat file.
* **Files:** `health_check.py`, `executar_check.bat`.

🔹 **System Information Reporter**
Collects essential system information and generates a structured .txt report.
* **Features:**
    * OS information and CPU details.
    * Machine and network name.
    * Automatic report generation.
* **Files:** `system_info.py`, `executar_info.bat`.

🔹 **File Organizer Tool**
A Python automation script that organizes files into folders based on file extensions.
* **Features:**
    * Automatically detects file extensions.
    * Creates destination folders dynamically.
    * Moves files safely.
* **Files:** `file_organizer.py`, `run_file_organizer.bat`.

🛠️ **Technologies**

* **Python 3.x**
* **Windows Batch (CMD)**
* **Standard Libraries:** `os`, `shutil`, `socket`, `platform`, `datetime`.
* **External Library:** `Requests` (used for API consumption).

📖 **How to Use**

1. Copy the desired Python scripts (.py) and Batch files (.bat) to a local folder.
2. For the **Currency Monitor**, ensure you install the dependency: `pip install requests`.
3. Run the corresponding .bat file to execute the automation with one click.

🎯 **Purpose**

These scripts were created for learning, practice, and portfolio purposes, simulating real-world IT Support and Infrastructure automation tasks.
