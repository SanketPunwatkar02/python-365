"""
Generate syllabus.json for the Python 365 project.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
CONTENT.mkdir(exist_ok=True)

topics = [
    # Module 1 – Python Fundamentals
    ("Variables and Data Types", "Python Fundamentals"),
    ("Input and Output", "Python Fundamentals"),
    ("Comments and Code Style", "Python Fundamentals"),
    ("Operators", "Python Fundamentals"),
    ("Type Conversion", "Python Fundamentals"),
    ("Strings", "Python Fundamentals"),
    ("String Methods", "Python Fundamentals"),
    ("Formatting Strings", "Python Fundamentals"),
    ("Numbers", "Python Fundamentals"),
    ("Booleans", "Python Fundamentals"),

    # Module 2 – Control Flow
    ("if Statements", "Control Flow"),
    ("if-else", "Control Flow"),
    ("Nested if", "Control Flow"),
    ("Match Case", "Control Flow"),
    ("For Loop", "Control Flow"),
    ("While Loop", "Control Flow"),
    ("Break and Continue", "Control Flow"),
    ("Range Function", "Control Flow"),
    ("Pass Statement", "Control Flow"),
    ("Mini Project", "Control Flow"),

    # Module 3 – Functions
    ("Functions", "Functions"),
    ("Arguments", "Functions"),
    ("Keyword Arguments", "Functions"),
    ("Return Values", "Functions"),
    ("Lambda Functions", "Functions"),
    ("Recursion", "Functions"),
    ("Variable Scope", "Functions"),
    ("Docstrings", "Functions"),
    ("Modules", "Functions"),
    ("Packages", "Functions"),

    # Module 4 – Collections
    ("Lists", "Collections"),
    ("List Methods", "Collections"),
    ("Tuples", "Collections"),
    ("Sets", "Collections"),
    ("Dictionaries", "Collections"),
    ("Dictionary Methods", "Collections"),
    ("Comprehensions", "Collections"),
    ("Nested Collections", "Collections"),
    ("Sorting", "Collections"),
    ("Searching", "Collections"),

    # Module 5 – Files
    ("Reading Files", "File Handling"),
    ("Writing Files", "File Handling"),
    ("CSV Files", "File Handling"),
    ("JSON Files", "File Handling"),
    ("Pathlib", "File Handling"),
    ("Exception Handling", "File Handling"),
    ("Custom Exceptions", "File Handling"),
    ("Logging", "File Handling"),
    ("Configuration Files", "File Handling"),
    ("Mini Project", "File Handling"),

    # Module 6 – OOP
    ("Classes", "Object Oriented Programming"),
    ("Objects", "Object Oriented Programming"),
    ("Constructors", "Object Oriented Programming"),
    ("Methods", "Object Oriented Programming"),
    ("Inheritance", "Object Oriented Programming"),
    ("Polymorphism", "Object Oriented Programming"),
    ("Encapsulation", "Object Oriented Programming"),
    ("Abstraction", "Object Oriented Programming"),
    ("Magic Methods", "Object Oriented Programming"),
    ("Dataclasses", "Object Oriented Programming"),

    # Module 7 – Advanced
    ("Decorators", "Advanced Python"),
    ("Generators", "Advanced Python"),
    ("Iterators", "Advanced Python"),
    ("Context Managers", "Advanced Python"),
    ("Virtual Environments", "Advanced Python"),
    ("Typing", "Advanced Python"),
    ("Enums", "Advanced Python"),
    ("Collections Module", "Advanced Python"),
    ("Functools", "Advanced Python"),
    ("itertools", "Advanced Python"),

    # Module 8 – Standard Library
    ("datetime", "Standard Library"),
    ("math", "Standard Library"),
    ("random", "Standard Library"),
    ("os", "Standard Library"),
    ("sys", "Standard Library"),
    ("subprocess", "Standard Library"),
    ("shutil", "Standard Library"),
    ("argparse", "Standard Library"),
    ("sqlite3", "Standard Library"),
    ("urllib", "Standard Library"),

    # Module 9 – Projects
    ("Calculator", "Projects"),
    ("Password Generator", "Projects"),
    ("Number Guessing Game", "Projects"),
    ("To-Do App", "Projects"),
    ("Expense Tracker", "Projects"),
    ("Weather App", "Projects"),
    ("Web Scraper", "Projects"),
    ("REST API Client", "Projects"),
    ("Portfolio Project", "Projects"),
    ("Final Project", "Projects"),
]

syllabus = []

for day in range(1, 366):
    topic, module = topics[(day - 1) % len(topics)]
    syllabus.append(
        {
            "day": day,
            "title": topic,
            "module": module,
        }
    )

output = CONTENT / "syllabus.json"

with output.open("w", encoding="utf-8") as f:
    json.dump(syllabus, f, indent=2, ensure_ascii=False)

print(f"Generated {len(syllabus)} lessons.")
print(output)
