"""Generate the project README from the current progress state."""

from __future__ import annotations

from pathlib import Path

from scripts.progress import load_progress
from scripts.utils import percentage, progress_bar

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
    for start, end, module_name in MODULES:
        if start <= day <= end:
            return module_name
    return "🚀 Getting Started"


def build_readme() -> str:
    progress = load_progress()

    current_day = progress["current_day"]
    total_days = progress["total_days"]
    current_topic = progress["current_topic"]
    last_release = progress["last_release"] or "Not yet"

    progress_percent = percentage(current_day, total_days)
    bar = progress_bar(current_day, total_days, 30)
    module = current_module(current_day)

    return f"""# 🐍 Python 365

> Learn Python in 365 days with automated daily publishing.

## Progress

**Day {current_day} / {total_days}**

```text
{bar}
```

**Completion:** {progress_percent}%

## Current Module

{module}

## Current Topic

{current_topic}

## Last Release

{last_release}

## Overview

This repository tracks a full year of Python practice, with each day building on the last.

### What the automation updates

- the next lesson content
- the progress record
- this README
- the published lesson index

"""


def save_readme() -> None:
    README_FILE.write_text(build_readme(), encoding="utf-8")


def main() -> None:
    save_readme()


if __name__ == "__main__":    main()