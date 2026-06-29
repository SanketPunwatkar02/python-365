"""
update_readme.py

Automatically regenerates the repository README
based on the current learning progress.
"""

from __future__ import annotations

from pathlib import Path

from scripts.progress import load_progress
from scripts.utils import progress_bar, percentage

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
    """Generate README.md content."""

    progress = load_progress()

    current_day = progress["current_day"]
    total_days = progress["total_days"]
    topic = progress["current_topic"]
    last_release = progress["last_release"] or "Not yet"

    percent = percentage(current_day, total_days)
    bar = progress_bar(current_day, total_days, 20)

    module = current_module(current_day)

    return f"""# 🐍 Python 365

> A complete **365-day Python learning journey** powered by GitHub Actions.

---

## 🎯 Goal

Learn Python from beginner to advanced by publishing one lesson every day.

This repository automatically:

- Generates lesson content
- Publishes one lesson daily
- Updates progress
- Rebuilds documentation
- Maintains a consistent GitHub contribution history

---

## 📈 Progress

**Day {current_day} / {total_days}**

```text
{bar}
