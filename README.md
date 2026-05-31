# Duplicate File Cleaner with Logging

# Overview

Duplicate File Cleaner with Logging is a Python automation tool that identifies and removes duplicate files from a specified directory and its subdirectories. The application uses MD5 checksum hashing to compare file contents and accurately detect duplicates, regardless of file names.

To maintain transparency and track operations, the tool automatically generates a log file containing details of all deleted files along with the total number of duplicates removed.

---

# Features

✔ Recursive directory traversal

✔ Duplicate file detection using MD5 checksum

✔ Automatic duplicate file removal

✔ Log file generation with timestamp

✔ Records deleted file names

✔ Displays total deleted file count

✔ Command-line based execution

✔ Supports nested subdirectories

---

# Technologies Used

* Python 3
* OS Module
* Sys Module
* Time Module
* Hashlib Module

---

# How It Works

1. User provides a directory path.
2. The application scans all files in the specified directory and subdirectories.
3. MD5 checksums are calculated for each file.
4. Files with identical checksums are identified as duplicates.
5. The first occurrence is preserved.
6. Remaining duplicate files are deleted.
7. Deleted file names are written to a log file.
8. A summary of deleted files is generated.

---

# Project Workflow

User Provides Directory Path
            │
            ▼
Scan Directory & Subdirectories
            │
            ▼
Generate MD5 Checksums
            │
            ▼
Identify Duplicate Files
            │
            ▼
Delete Duplicate Copies
            │
            ▼
Generate Log File
            │
            ▼
Store Deleted File Names
            │
            ▼
Display Completion Message

---

# Usage

Run the script using:

python DuplicateCleaner.py "DirectoryPath"


Example:

python DuplicateCleaner.py "D:\TestFolder"


---

# Sample Folder Structure


TestFolder
│
├── file1.txt
├── copy_file1.txt
│
└── Backup
    └── copy_file2.txt


After execution:


TestFolder
│
├── file1.txt
│
└── Backup


Duplicate files are removed while one original copy is preserved.

---

# Sample Log File


------------------------------------------------------
This is a log file of Automation Script
This is a directory cleaner Script
------------------------------------------------------
This is created at
Fri May 30 16:30:20 2026
------------------------------------------------------

Deleted file : copy_file1.txt
Deleted file : copy_file2.txt

Total deleted file : 2


---

# Project Structure


Duplicate-File-Cleaner-With-Logging/
│
├── DuplicateCleaner.py
├── README.md
├── Demo/
│   ├── file1.txt
│   ├── copy_file1.txt
│   └── SubFolder/
│       └── copy_file2.txt
│
└── Logger*.log

---

# Future Enhancements

* GUI interface using Tkinter
* Move files to Recycle Bin instead of permanent deletion
* Email notification support
* Advanced logging using Python Logging Module
* File filtering by extension
* Scheduled automatic execution

---

# Learning Outcomes

This project demonstrates practical experience with:

* File Handling
* Directory Traversal
* Hashing Algorithms (MD5)
* Python Automation
* Logging Mechanisms
* Data Structures (Dictionary)
* Command Line Programming

---


Python Developer | Automation Enthusiast
