"""
publish.py

Main publishing engine for Python 365.

Workflow:
1. Load current progress.
2. Determine next lesson.
3. Copy lesson from content/ to published/.
4. Update progress.
5. Regenerate README.
6. Regenerate lesson index.
"""

from __future__ import annotations
from scripts.progress import load_progress
from scripts.build_index import save_index
from scripts.update_readme import save_readme
from scripts.utils import ensure_directory
import json
import shutil
from datetime import datetime
from pathlib import Path

from build_index import save_index
from progress import load_progress, save_progress
from update_readme import save_readme

ROOT = Path(__file__).resolve().parent.parent

CONTENT_DIR = ROOT / "content"
PUBLISHED_DIR = ROOT / "published"
SYLLABUS_FILE = CONTENT_DIR / "syllabus.json"


def load_syllabus() -> dict[int, dict]:
    """Load syllabus metadata."""

    with SYLLABUS_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return {lesson["day"]: lesson for lesson in data}


def publish_lesson(day: int) -> None:
    """Copy one lesson into the published directory."""

    source = CONTENT_DIR / f"Day{day:03d}"
    destination = PUBLISHED_DIR / f"Day{day:03d}"

    if not source.exists():
        raise FileNotFoundError(f"Lesson folder missing: {source}")

    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def update_progress(day: int, syllabus: dict[int, dict]) -> None:
    """Update progress.json."""

    progress = load_progress()

    lesson = syllabus.get(day, {})

    progress["current_day"] = day
    progress["current_topic"] = lesson.get("title", f"Day {day}")
    progress["last_release"] = datetime.utcnow().strftime("%Y-%m-%d")

    save_progress(progress)


def main() -> None:
    progress = load_progress()
    syllabus = load_syllabus()

    next_day = progress["current_day"] + 1

    if next_day > progress["total_days"]:
        print("✅ All 365 lessons have already been published.")
        return

    print(f"Publishing Day {next_day:03d}...")

    publish_lesson(next_day)

    update_progress(next_day, syllabus)

    save_readme()

    save_index()

    print(f"✅ Day {next_day:03d} published successfully.")


if __name__ == "__main__":
    main()
