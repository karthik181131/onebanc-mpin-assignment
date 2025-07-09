# MPIN Strength Checker – OneBanc Task

This is a simple Python project that checks if a user's MPIN (4 or 6 digits) is strong or weak.

You can check MPIN strength either through the **Command-Line Interface (CLI)** or a **user-friendly Web Interface**, both included in this project.

1.Run this to test interactively via terminal.
```bash
python run.py

2.web interface (flask):
```bash
python run.py
** Access it at: http://127.0.0.1:5000


** Run the Test Cases (Validation)
''''bash
 python -m src.test_cases


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


# MPIN Strength Checker – OneBanc Task

🔗 [Click here to view the full project on GitHub](https://github.com/karthik181131/onebanc-mpin-assignment)

✍️ Author
Boddepalli Karthik 
GMR Institute of Technology 
B.Tech – CSE (AI & DS)



