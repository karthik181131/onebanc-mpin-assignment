# MPIN Strength Checker – OneBanc Task

This is a simple Python project that checks if a user's MPIN (4 or 6 digits) is strong or weak.

You can check MPIN strength either through the Command-Line Interface (CLI) or a user-friendly Web Interface, both included in this project.


1.Run this to test interactively via terminal.
```bash
python run.py

## 💻 Command Line Interface (CLI)

This is how the MPIN strength is checked via terminal:
![CLI Demo](screenshots/cli_demo.png)
---

2.web interface (flask):
```bash
python run.py
** Access it at: http://127.0.0.1:5000

## 🌐 Web Interface (Flask)

Check MPIN strength using a simple web UI:
![Web UI Screenshots](screenshots/web_ui.png)
---


** Run the Test Cases (Validation)
''''bash
 python -m src.test_cases
 
 ![Test Cases Result](screenshots/test_cases.png)




📁 Folder Structure

mpin_task/
├── data/
│   └── common_mpins.txt         # Contains a list of commonly used MPINs.
│
├── src/
│   ├── checker.py               # Core logic for validating MPIN strength.
│   ├── test_cases.py            # Automated test suite to validate checker logic.
│   └── __init__.py              # Marks 'src' as a Python package.
│
├── templates/
│   └── index.html               # HTML template for the Flask web interface.
│
├── run.py                       # Command-line interface to run the MPIN checker.
├── app.py                       # Flask-based web application for interactive input.
├── README.md                    # Documentation with instructions, usage, and features.


✍️ Author
Boddepalli Karthik 
GMR Institute of Technology 
B.Tech – CSE (AI & DS)



