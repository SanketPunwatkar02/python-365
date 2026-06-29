"""
generate_lessons.py

Generate the complete 365-day lesson structure for Python 365.

This script creates the entire course skeleton inside the `content/`
directory. Each lesson includes a consistent set of Markdown and Python
files that can later be filled with real educational content.

Run:

    python scripts/generate_lessons.py
"""

from __future__ import annotations

from pathlib import Path

from utils import ensure_directory, write_text, day_folder

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = ROOT / "content"

TOTAL_DAYS = 365


def create_readme(day: int) -> str:
    return f"""# Day {day:03d}

# Title

> Replace with today's topic.

---

## Learning Objectives

- Understand ...
- Learn ...
- Practice ...

---

Estimated Time: 20-30 minutes

Difficulty: ⭐☆☆☆☆
"""


def create_lesson() -> str:
    return """# Lesson

Write the theory for today's lesson here.

Explain concepts with examples and diagrams if needed.
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

Write your solution below.
"""

# TODO: Solve the exercise.
'''


def create_solution() -> str:
    return '''"""
Reference Solution
"""

# TODO: Add the reference solution.
'''


def create_quiz() -> str:
    return """# Quiz

1. Question 1

2. Question 2

3. Question 3

Answers:

-
-
-
"""


def create_notes() -> str:
    return """# Notes

Important points

- ...

Common mistakes

- ...

Tips

- ...
"""


def generate_day(day: int) -> None:
    folder = CONTENT_DIR / day_folder(day)

    ensure_directory(folder)

    files = {
        "README.md": create_readme(day),
        "lesson.md": create_lesson(),
        "example.py": create_example(),
        "exercise.py": create_exercise(),
        "solution.py": create_solution(),
        "quiz.md": create_quiz(),
        "notes.md": create_notes(),
    }

    for filename, content in files.items():
        path = folder / filename

        if not path.exists():
            write_text(path, content)


def main() -> None:
    ensure_directory(CONTENT_DIR)

    print(f"Generating {TOTAL_DAYS} lesson templates...\n")

    for day in range(1, TOTAL_DAYS + 1):
        generate_day(day)

    print(f"Successfully generated {TOTAL_DAYS} lesson folders.")


if __name__ == "__main__":
    main()
