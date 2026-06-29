"""
generate_lessons.py

Generate the complete 365-day lesson structure for Python 365.

Creates lesson folders inside the content directory using
information from syllabus.json.

Run:
    python -m scripts.generate_lessons
"""

from __future__ import annotations

import json
from pathlib import Path

from scripts.utils import (
    day_folder,
    ensure_directory,
    write_text,
)

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = ROOT / "content"
SYLLABUS_FILE = CONTENT_DIR / "syllabus.json"

TOTAL_DAYS = 365


def load_syllabus() -> list[dict]:
    """Load syllabus.json."""

    if not SYLLABUS_FILE.exists():
        raise FileNotFoundError(
            f"Missing syllabus file: {SYLLABUS_FILE}"
        )

    with SYLLABUS_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def create_readme(day: int, title: str) -> str:
    return f"""# 🐍 Day {day:03d} - {title}

> Python 365 Daily Lesson

---

## 🎯 Learning Objectives

- Understand today's topic
- Learn through examples
- Complete the exercise
- Test yourself with the quiz

---

## 📚 Lesson Files

| File | Purpose |
|------|---------|
| lesson.md | Theory |
| example.py | Example program |
| exercise.py | Practice problems |
| solution.py | Reference solution |
| quiz.md | Self assessment |
| notes.md | Additional notes |

---

## Estimated Time

20–30 minutes

## Difficulty

⭐☆☆☆☆
"""


def create_lesson(title: str) -> str:
    return f"""# {title}

## Introduction

Write today's lesson here.

---

## Explanation

Explain the topic with examples.

---

## Key Points

- Point 1
- Point 2
- Point 3
"""


def create_example() -> str:
    return '''"""
Example Program
"""


def main():
    print("Hello from Python 365!")


if __name__ == "__main__":
    main()
'''


def create_exercise() -> str:
    return '''"""
Exercise

Complete the task below.
"""

# TODO: Write your solution here.
'''


def create_solution() -> str:
    return '''"""
Reference Solution
"""

# TODO: Add solution.
'''


def create_quiz() -> str:
    return """# Quiz

1. Question 1

2. Question 2

3. Question 3

---

## Answers

-
-
-
"""


def create_notes() -> str:
    return """# Notes

## Important Points

-

-

-

## Common Mistakes

-

-

-

## Tips

-

-

-
"""


def generate_day(day: int, title: str) -> None:
    folder = CONTENT_DIR / day_folder(day)

    ensure_directory(folder)

    files = {
        "README.md": create_readme(day, title),
        "lesson.md": create_lesson(title),
        "example.py": create_example(),
        "exercise.py": create_exercise(),
        "solution.py": create_solution(),
        "quiz.md": create_quiz(),
        "notes.md": create_notes(),
    }

    for filename, content in files.items():
        file_path = folder / filename

        if not file_path.exists():
            write_text(file_path, content)


def main() -> None:

    ensure_directory(CONTENT_DIR)

    syllabus = load_syllabus()

    print("====================================")
    print("Generating Python 365 lesson files...")
    print("====================================")

    created = 0

    for lesson in syllabus:

        day = lesson["day"]
        title = lesson["title"]

        generate_day(day, title)

        created += 1

        print(f"✓ Day {day:03d} - {title}")

    print("\n====================================")
    print(f"Successfully generated {created} lesson folders.")
    print("====================================")


if __name__ == "__main__":
    main()
