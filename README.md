# IT Automation Scripts for IT Support

📋 **Description**

This repository contains a collection of Python automation scripts designed to assist IT Support and Infrastructure teams with common operational tasks such as system health checks, system information reporting, and file organization. 
The tools are lightweight, portable, and focused on improving troubleshooting efficiency and operational productivity.

🚀 **Available Tools**

🔹**NetPulse - Network Health Monitor**
A real-time network stability tool that tracks latency and connection quality.
* **Features:**
    * Real-time Latency Tracking: Measures ping in milliseconds with high precision.
    * Visual Status Alerts: Color-coded terminal output for Stable, High Latency, or Connection Drop.
    * Audit Logging: Automatically saves all connection events to `networking_health.log`for troubleshooting.
    * One-click Execution: Includes a .bat file to run the monitor in a dedicated window.
* **What I learned:** System process interaction via `subprocess`, handling real-time data loops, and conditional status reporting.
* **Files:** `netpulse_monitor.py`, `run_netpulse.bat`.

🔹**Network Security Port Scanner**
A security auditing tool designed to identify open ports and potential vulnerabilities in a network host.
* **Features:**
    * Scans common service ports (SSH, HTTP, RDP, etc.).
    * Real-time connection testing using socket programming.
    * Generates security audit logs for compliance tracking.
* **What I learned:** Networks protocols, socket timeouts, and handling network-level exceptioins.
* **Files:** `port_scanner.py`, `run_port_scanner.bat`.

🔹 **Web Availability & Latency Checker**
A connectivity tool to check if a website is online and measure its response time.
* **Features:**
    * Checks if a URL is up (Online/Offline status).
    * Measures latency (ping) in milliseconds.
    * Performs multiple attempts with timed intervals.
    * Automatic logging of results in `web_monitor_log.txt`.
* **What I learned:** Measuring execution time and managing connection timeouts.
* **Files:** `web_monitor.py`, `run_web_monitor.bat`.

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
* **Standard Libraries:** `os`, `shutil`, `socket`, `platform`, `datetime`, `subprocess`, `time`.
* **External Library:** `Requests` (used for API consumption).

📖 **How to Use**

1. Copy the desired Python scripts (.py) and Batch files (.bat) to a local folder.
2. For the **Currency Monitor** and **Web Monitor**, ensure you install the dependency: ```bash
pip install requests
3. Run the corresponding .bat file to execute the automation with one click.

🎯 **Purpose**

These scripts were created for learning, practice, and portfolio purposes, simulating real-world IT Support and Infrastructure automation tasks.
