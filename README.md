# IT Automation Scripts | Python Portfolio for Support, Infrastructure & Operations

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Automation](https://img.shields.io/badge/Focus-IT%20Automation-green)
![Status](https://img.shields.io/badge/Project-Active-brightgreen)

## 📌 Overview

This repository contains a collection of practical **Python automation tools** focused on real-world IT operations.

Projects were developed to simulate and solve common tasks related to:

- IT Support  
- Infrastructure  
- Monitoring  
- Help Desk  
- File Management  
- Reporting  
- Operational Productivity  

All tools are lightweight, objective, and designed for Windows environments.

---

## 🚀 Highlights

✔ 18+ Practical Python Projects  
✔ Real Operational Use Cases  
✔ CLI Tools & Automation Scripts  
✔ Monitoring / Reports / Logging  
✔ Support & Infrastructure Focus  
✔ Constantly Updated Portfolio

---

## 📁 Repository Structure

```text
it-automation-scripts
│
README.md
│
automation
│   backup_automation.py
│   file_organizer.py
│   screenshot_organizer.py
│   run_file_organizer.bat
│   run_screenshot_org.bat
│
business
│   attendance_logger.py
│   payroll_cli_v1.py
│   payroll_cli_v1.bat
│
finance
│   currency_monitor.py
│   expense_tracker_cli.py
│   run_monitor.bat
│
monitoring
│   disk_usage_audit.py
│   log_analyzer.py
│   resource_monitor.py
│   resource_dashboard.bat
│
network
│   netpulse_monitor.py
│   port_scanner.py
│   web_monitor.py
│   run_netpulse.bat
│   run_port_scanner.bat
│   run_web_monitor.bat
│
office_automation
│   excel_sales_report_email.py
│
security
│   file_hasher.py
│   run_integrity_check.bat
│   user_access_audit
|
support
|   daily_it_task_logger.py
|   it_asset_inventory.py
|   password_reset_request.py
│   support_ticket_manager.py
│
system
│   health_check.py
│   host_inventory.py
│   system_cleaner.py
│   system_info.py
│   executar_check.bat
│   executar_info.bat
│   host_inventory.bat
│   run_cleanup.bat
```

---

## 📂 Folder Overview

- **automation** → file management, backup and workflow automation tools  
- **business** → business logic, attendance and administrative tools  
- **finance** → financial monitoring and expense tracking tools  
- **monitoring** → logs, resource usage and disk analysis tools  
- **network** → connectivity, scanning, latency and uptime tools  
- **office_automation** → Excel processing and email automation  
- **security** → integrity verification and auditing tools  
- **support** → help desk systems, dashboards and IT asset management  
- **system** → diagnostics, maintenance and inventory scripts

---

## 🛠️ Featured Projects

### 🔹 User Access Audit Tool

Tracks user access changes (granted or removed) and stores records in a `.csv` file for auditing purposes.

**Skills Demonstrated:**

- CSV file handling  
- Data persistence  
- Timestamp automation  
- CLI menu systems  
- Basic security and audit concepts  

**Files:** `user_access_audit.py`

---

### 🔹 Daily IT Task Logger

Registers completed IT tasks through terminal input and saves records into a `.txt` history file.

**Skills Demonstrated:**

- `while True` loops
- File persistence
- Timestamp automation
- CLI menu systems
- Operational workflow logic

**Files:** `daily_it_task_logger.py`

---

### 🔹 Password Reset Request Dashboard

A web-based internal support system built with Python and Flask to register employee password reset requests.

**Skills Demonstrated:**

- Flask web development  
- HTML + CSS forms  
- Request tracking workflow  
- Priority classification  
- Timestamp automation  
- Python backend logic  

**Files:** `password_reset_request.py`

---

### 🔹 IT Asset Inventory Dashboard

A web-based inventory system built with Python and Flask for registering and tracking IT assets in a corporate environment.

**Skills Demonstrated:**

- Flask web development  
- HTML + CSS interface  
- Form handling  
- IT asset lifecycle tracking  
- Operational workflow logic  
- Python backend fundamentals  

**Files:** `it_asset_inventory.py`

---

### 🔹 Employee Attendance Logger

A command-line attendance tool that registers employee check-ins with automatic timestamps and stores records in `.txt` files.

**Skills Demonstrated:**

- `while True` loops  
- Input validation  
- File persistence  
- Timestamp automation  

**Files:** `attendance_logger.py`

---

### 🔹 Automated File Backup Tool

Creates full folder backups with timestamped names to preserve previous versions.

**Skills Demonstrated:**

- `shutil.copytree()`  
- Path validation  
- Backup workflow logic  
- File system automation  

**Files:** `backup_automation.py`

---

### 🔹 Disk Usage Analyzer

Scans folders, calculates size usage, sorts results, and exports reports.

**Skills Demonstrated:**

- Recursive scanning  
- `os.walk()`  
- Human-readable formatting  
- Reporting automation  

**Files:** `disk_usage_audit.py`

---

### 🔹 Sales Report Automation

Reads Excel spreadsheets, calculates KPIs, and sends Outlook email reports.

**Skills Demonstrated:**

- `pandas`  
- Data aggregation  
- HTML reports  
- Outlook automation  

**Files:** `excel_sales_report_email.py`

---

### 🔹 Support Ticket Manager

CLI Help Desk workflow using persistent JSON storage.

**Skills Demonstrated:**

- CRUD logic  
- JSON persistence  
- Menu systems  

**Files:** `support_ticket_manager.py`

---

### 🔹 Network Port Scanner

Scans common ports and identifies open services.

**Skills Demonstrated:**

- `socket`  
- Network logic  
- Security auditing  

**Files:** `port_scanner.py`

---

### 🔹 System Resource Monitor

Displays live CPU and RAM usage directly in terminal.

**Skills Demonstrated:**

- `psutil`  
- Real-time loops  
- Terminal dashboards  

**Files:** `resource_monitor.py`

---

### 🔹 File Integrity Auditor

Generates SHA-256 hashes to verify files.

**Skills Demonstrated:**

- Cryptography  
- Binary file reading  
- Security automation  

**Files:** `file_hasher.py`

---

## 📚 Technologies Used

### Languages

- **Python 3.x**  
- **Windows Batch (.bat)**

### Core Libraries

- `os`
- `shutil`
- `datetime`
- `hashlib`
- `socket`
- `subprocess`
- `time`
- `json`
- `platform`

### External Libraries

- `pandas`
- `requests`
- `psutil`
- `pywin32`

---

## 📖 How to Run

### 1. Clone Repository

```bash
git clone https://github.com/hericlesfsr/it-automation-scripts.git
```

### 2. Install Dependencies

```bash
pip install pandas requests psutil pywin32
```

### 3. Run Example

```bash
python attendance_logger.py
```

---

## 🎯 Purpose

This portfolio was built to demonstrate practical Python skills applied to:

- IT Support routines  
- Operational automation  
- Infrastructure tasks  
- Monitoring solutions  
- Productivity improvements  

---

## 👨‍💻 Ideal For

- Recruiters hiring Junior Python Developers  
- IT Support / Help Desk roles  
- Infrastructure Analyst roles  
- NOC positions  
- Automation-focused opportunities  

---

## 📈 Recent Additions

- User Access Audit Tool
- Daily IT Task Logger
- Password Reset Request Dashboard

---

## 📬 Contact

- **GitHub:** https://github.com/hericlesfsr  
- **LinkedIn:** https://linkedin.com/in/hericles-rozendo

---

## ⭐ If you found this repository useful, feel free to star it.
