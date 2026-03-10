# Python Automation and Operational Tools
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Automation](https://img.shields.io/badge/Focus-IT%20Automation-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

📋 **Description**

This repository contains a collection of **Python automation tools** designed to assist IT Support, Infrastructure, and Operations teams with common operational tasks such as system diagnostics, monitoring, and workflow automation.

The tools are lightweight, portable, and focused on improving troubleshooting efficiency and operational productivity in real-world IT environments.

---

## Repository Structure
```
it-automation-scripts
│
README.md
│
automation
│   file_organizer.py
│   run_file_organizer.bat
│   screenshot_organizer.py
│   run_screenshot_org.bat
│
system
│   system_info.py
│   executar_info.bat
│   health_check.py
│   executar_check.bat
│   system_cleaner.py
│   run_cleanup.bat
│   host_inventory.py
│   host_inventory.bat
│
network
│   port_scanner.py
│   run_port_scanner.bat
│   netpulse_monitor.py
│   run_netpulse.bat
│   web_monitor.py
│   run_web_monitor.bat
│
monitoring
│   resource_monitor.py
│   resource_dashboard.bat
│
security
│   file_hasher.py
│   run_integrity_check.bat
│
support
│   support_ticket_manager.py
│
business
│   payroll_cli_v1.py
│   payroll_cli_v1.bat
│
finance
│   currency_monitor.py
│   run_monitor.bat
```

### Folder Overview

- **automation** → file management and workflow automation scripts
- **system** → system diagnostics, inventory, and maintenance tools
- **network** → network monitoring and security utilities
- **monitoring** → system resource monitoring tools
- **security** → file integrity and auditing utilities
- **support** → help desk workflow simulation tools
- **business** → business logic simulation projects
- **finance** → financial and market monitoring tools

---

🚀 **Projects**
Below are some of the automation tools included in this repository.

---

🔹 **Log Analyzer Tool**
A lightweight CLI tool that scans system log files and extracts operational events such as errors, warnings, and failed login attempts.

* **Features:**
    * Log Parsing: Reads log files line by line.
    * Error Detection: Counts occurrences of "error".
    * Warning Detection: Identifies warning events.
    * Failed Login Detection: Tracks authentication failures.
    * Report Generation: Generates a structured `log_report.txt` summary.

* **What I learned:**
    * Text parsing in Python
    * File reading and iteration
    * Pattern detection in log files
    * Report generation and file writing

* **File:** `log_analyzer.py`

---

🔹 **Host Inventory CLI Tool**
A lightweight command-line tool that collects basic system information from the local machine and generates a structured inventory report.

* **Features:**
    * Hostname Detection: Automatically retrieves the computer name.
    * Local IP Identification: Captures the machine's current IP address.
    * Operating System Info: Displays OS name and version.
    * Logged-in User Detection: Identifies the active system user.
    * Automatic Report Generation: Exports the collected information into a `.txt` inventory file.
    * Lightweight Execution: Runs instantly from the terminal with no external dependencies.
* **What I learned:**
    * Working with Python standard libraries (`socket`, `platform`, `os`)
    * Collecting system-level information programmatically
    * Structuring CLI scripts with functions
    * File creation and writing using `with open()`
    * Formatting terminal output for readability
* **Files:** `host_inventory.py`, `host_inventory.bat`

---

🔹 **CLI Ticket Management System (Help Desk Workflow Simulation)**  
A command-line ticket management tool that simulates a basic Help Desk workflow.  
It allows users to create, store, and list support tickets using persistent JSON storage.
* **Features:**
    * Ticket Creation: Register new support requests with title and description.
    * JSON Storage: Saves all tickets in a structured `.json` file.
    * Ticket Listing: Displays all registered tickets directly in the CLI.
    * Menu-driven Interface: Simple interactive terminal navigation.
    * Persistent Data: Tickets remain saved between executions.
    * Lightweight Design: Runs entirely in the terminal without external dependencies.
* **What I learned:**
    * JSON data persistence in Python
    * Structuring CLI applications
    * Menu-driven program logic
    * File reading and writing operations
    * Handling user input and validation
* **Files:** `support_ticket_manager.py`

---

🔹 **Payroll CLI System (Business Logic Simulation)**
A command-line payroll processing system that models real-world Brazilian payroll rules with structured business logic and persistent logging.
* **Features:**
    * Gross Salary Calculation: Based on hourly rate and worked hours.
    * Progressive INSS Calculation: Applies tier-based social security rates.
    * IRRF Computation: Calculates income tax using base deduction rules.
    * Union Fee Deduction: Automatic percentage-based calculation.
    * Net Salary Output: Structured and formatted CLI display.
    * Persistent Logging: Appends payroll records into a `.txt` file with timestamp.
    * Multi-Employee Support: Loop-based execution for batch processing.
    * One-click Execution: Includes `.bat` launcher for simplified runtime.
* **What I learned:**
    * Business rule modeling in Python
    * Progressive tax logic implementation
    * File handling using `with open()` context manager
    * Data formatting and financial precision handling
    * Timestamp logging with `datetime`
    * Structured CLI user interaction
* **Files:** `payroll_cli_v1.py`, `payroll_cli_v1.bat`

---

🔹 **Smart Screenshot Organizer (Advanced Workflow)**
A professional-grade automation tool designed to eliminate folder clutter by restructuring local files into a logical chronological hierarchy.
* **Features:**
    * Dynamic Path Discovery: Robust logic to identify OneDrive and local image directories across various Windows configurations.
    * Smart Pattern Matching: Detects standard Windows capture naming conventions (e.g., "Captura de tela" and "Screenshot").
    * Chronological Sorting: Automatically creates and moves files into month-based folders (e.g., 2026-02 (Prints)) based on file metadata.
* **What I learned:** Abstract path management, system environment variables, and automated file-system restructuring.
* **Files:** `screenshot_organizer.py`, `run_screenshot_org.bat`

---

🔹 **Digital Integrity Auditor (Security Tool)**
A security-focused utility that generates unique cryptographic signatures (SHA-256) to verify file authenticity and detect tampering.
* **Features:**
    * Cryptographic Precision: Uses the industry-standard SHA-256 algorithm for reliable integrity checks.
    * Efficient Streaming: Processes files in 4096-byte chunks to handle large files (ISOs, Databases) without high memory consumption.
    * Interactive CLI: Supports drag-and-drop input for rapid operational auditing.
* **What I learned:** Cryptography concepts, binary data streaming, and interactive shell sanitization.
* **Files:** `file_hasher.py`, `run_integrity_check.bat`

---

🔹 **System Resource Monitor (Real-Time Dashboard)**
A real-time performance monitoring tool that displays CPU and RAM usage directly in the terminal using a visual dashboard.
* **Features:**
    * Real-time CPU and memory tracking
    * Terminal dashboard with visual progress bars
    * Automatic screen refresh for live monitoring
    * Critical usage alerts for high resource consumption
    * One-click execution via a .bat launcher
* **What I learned:** System resource monitoring with external libraries, terminal visualization techniques, and real-time data loops.
* **Files:** `resource_monitor.py`, `resource_dashboard.bat`

---

🔹 **System Cleanup Automation (High Impact)**
A powerful maintenance tool designed to wipe out temporary files and optimize Windows performance.
* **Features:**
    * Deep Scan: Targets multiple system and user temporary directories.
    * Resilient Execution: Advanced exception handling to bypass files in use.
    * Privilege Awareness: Detects and reports missing Administrative rights for restricted folders.
    * Automated Summary: Provides a final report of total items removed vs. items kept for security.
* **What I learned:** Advanced file system manipulation, OS environment variables, and professional error handling for system-level scripts.
* **Files:** `system_cleaner.py`, `run_cleanup.bat`

---

🔹 **NetPulse - Network Health Monitor**
A real-time network stability tool that tracks latency and connection quality.
* **Features:**
    * Real-time Latency Tracking: Measures ping in milliseconds.
    * Visual Status Alerts: Terminal indicators for Stable, High Latency, or Connection Drop.
    * Event Logging: Saves connection events to `network_health.log` for troubleshooting.
* **What I learned:** System process interaction via `subprocess`, handling real-time data loops, and conditional status reporting.
* **Files:** `netpulse_monitor.py`, `run_netpulse.bat`

---

🔹 **Network Security Port Scanner**
A security auditing tool designed to identify open ports and potential vulnerabilities in a network host.
* **Features:**
    * Scans common service ports (SSH, HTTP, RDP, etc.).
    * Real-time connection testing using socket programming.
    * Generates security audit logs for compliance tracking.
* **What I learned:** Network protocols, socket timeouts, and handling network-level exceptions.
* **Files:** `port_scanner.py`, `run_port_scanner.bat`

---

🔹 **Web Availability & Latency Checker**
A connectivity tool to check if a website is online and measure its response time.
* **Features:**
    * Checks if a URL is up (Online/Offline status).
    * Measures latency (ping) in milliseconds.
    * Performs multiple attempts with timed intervals.
    * Automatic logging of results in `web_monitor_log.txt`
* **What I learned:** Measuring execution time and managing connection timeouts.
* **Files:** `web_monitor.py`, `run_web_monitor.bat`

---

🔹 **Currency & Market Monitor**
A real-time financial monitoring tool that connects to external APIs to fetch currency exchange rates.
* **Features:**
    * Real-time data for USD, EUR, and BTC.
    * Integration with REST APIs (JSON handling).
    * Automatic history logging in .txt format.
    * One-click execution via .bat file.
* **Files:** `currency_monitor.py`, `run_monitor.bat`

---

🔹 **System Health Check**
A portable diagnostic tool developed in Python to perform quick system health checks.
* **Features:**
    * Checks available disk space.
    * Verifies internet connectivity.
    * Designed for fast troubleshooting.
    * Portable execution via .bat file.
* **Files:** `health_check.py`, `executar_check.bat`

---

🔹 **System Information Reporter**
Collects essential system information and generates a structured .txt report.
* **Features:**
    * OS information and CPU details.
    * Machine and network name.
    * Automatic report generation.
* **Files:** `system_info.py`, `executar_info.bat`

---

🔹 **File Organizer Tool**
A Python automation script that organizes files into folders based on file extensions.
* **Features:**
    * Automatically detects file extensions.
    * Creates destination folders dynamically.
    * Moves files safely.
* **Files:** `file_organizer.py`, `run_file_organizer.bat`

---

🛠️ **Technologies**

* **Python 3.x**
* **Windows Batch (CMD)**
* **Core Libraries:** `os`, `shutil`, `hashlib`, `socket`, `platform`, `datetime`, `subprocess`, `time`
* **External Libraries:** `requests`, `psutil`

---

📖 **How to Use**

1. Clone the repository: 
```bash 
git clone https://github.com/hericlesfsr/it-automation-scripts.git
```
2. Setup Environment:
It is highly recommended to use a virtual environment (`.venv`) for dependency isolation.
3. Install Dependencies: 
```bash
pip install requests psutil
```
4. **Execution:** 
* **Standard tools:** Double-click the corresponding `.bat` file for automated execution via Python.
* **System Cleaner:** Right-click `run_cleanup.bat` and select **"Run as Administrator"** to ensure full access to temporary system directories.
* **Integrity Auditor:** Run `run_integrity_check.bat` and drag any file into the terminal to generate its SHA-256 signature.

---

👨‍💻 Who Is This For?

This repository is ideal for:

* **IT Support and Help Desk professionals**
* **Junior System Administrators**
* **Infrastructure and NOC analysts**
* **Students building an automation portfolio**
* **Anyone learning Python for real-world operational tasks**

---

🎯 **Purpose**

These projects simulate real-world operational scenarios in IT Support, Infrastructure, Security, and Business Logic environments.

The main objective is to demonstrate practical automation skills using Python to improve operational efficiency, troubleshooting workflows, and system observability.
---
