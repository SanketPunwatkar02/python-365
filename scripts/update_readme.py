"""
update_readme.py

Automatically regenerates the repository README based on the current
learning progress.

This script should be called after each lesson is published.
"""

from __future__ import annotations

from pathlib import Path

from progress import load_progress
from utils import progress_bar, percentage

ROOT = Path(__file__).resolve().parent.parent

README_FILE = ROOT / "README.md"


MODULES = [
    (1, 30, "🐍 Python Fundamentals"),
    (31, 60, "🔀 Control Flow"),
    (61, 90, "⚙️ Functions"),
    (91, 120, "📦 Data Structures"),
    (121, 150, "📁 File Handling"),
    (151, 210, "🏛️ Object-Oriented Programming"),
    (211, 260, "🚀 Advanced Python"),
    (261, 300, "📚 Standard Library"),
    (301, 365, "🛠️ Projects"),
]


def current_module(day: int) -> str:
    """Return the current learning module."""

    for start, end, name in MODULES:
        if start <= day <= end:
            return name

    return "🚀 Getting Started"


def build_readme() -> str:
    """Generate README markdown."""

    progress = load_progress()

    current_day = progress["current_day"]
    total_days = progress["total_days"]

    bar = progress_bar(current_day, total_days, 20)
    percent = percentage(current_day, total_days)

    module = current_module(current_day)

    return f"""# 🐍 Python 365

> Learn Python from beginner to advanced through one lesson every day.

---

## 🎯 Project Goal

Python 365 is a self-publishing learning platform that automatically
releases one Python lesson every day using GitHub Actions.

The objective is to build Python skills consistently while maintaining
a professional GitHub repository.

---

## 📈 Progress

**Day {current_day} / {total_days}**

```text
{bar}

{percent:.2f}% Complete
