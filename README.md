# FUTURE_CS_02 - Password Strength Analyzer Tool

## Overview
The **Password Strength Analyzer Tool** is a Python-based application designed to assess the strength of user passwords, provide real-time improvement feedback, and enhance security by hashing passwords using SHA-256. Featuring a user-friendly graphical interface built with tkinter, this tool is ideal for both everyday users and professionals.

## Features
- **Password Evaluation:** Checks for:
  - Minimum length (8 characters)
  - Presence of uppercase and lowercase letters
  - Inclusion of numerical digits
  - Use of special characters (e.g., @, #, $)
- **Real-Time Feedback:** Offers actionable suggestions to improve weak or moderate passwords.
- **Secure Hashing:** Implements SHA-256 to securely handle passwords without storing plaintext.
- **Graphical User Interface:** Built with tkinter for intuitive use.

## Technology Stack
- **Programming Language:** Python
- **Key Libraries:**
  - `tkinter` – for building the GUI.
  - `re` – for regex-based password evaluation.
  - `hashlib` – for SHA-256 password hashing.

## Project Structure
- `src/`  
  Contains the source code for the password analyzer tool.
- `docs/`  
  Documentation and project reports.
- `tests/`  
  Automated test cases and validation scripts.
- `README.md`  
  This file.

## Installation & Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/FirdawsM/FUTURE_CS_02.git

Navigate to the Project Directory:
 `
    cd FUTURE_CS_02 `

Run Application:

``` bash

python src/main.py
