"""
progress.py

Handles reading, validating, and updating the project's progress.json file.

This module acts as the single source of truth for tracking the current
lesson published by the automation engine.
"""

from __future__ import annotations
from scripts.progress import load_progress
from scripts.build_index import save_index
from scripts.update_readme import save_readme
from scripts.utils import ensure_directory
import json
from pathlib import Path
from typing import Any, Dict

# Root directory of the repository
ROOT_DIR = Path(__file__).resolve().parent.parent

PROGRESS_FILE = ROOT_DIR / "progress.json"

DEFAULT_PROGRESS = {
    "current_day": 0,
    "total_days": 365,
    "current_topic": "Not Started",
    "last_release": None,
}


class ProgressError(Exception):
    """Raised when progress data is invalid."""


def load_progress() -> Dict[str, Any]:
    """
    Load progress.json.

    Returns:
        Dictionary containing progress information.

    Raises:
        FileNotFoundError
        ProgressError
    """

    if not PROGRESS_FILE.exists():
        raise FileNotFoundError(
            f"Progress file not found: {PROGRESS_FILE}"
        )

    try:
        with PROGRESS_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise ProgressError("Invalid JSON in progress.json") from exc

    validate_progress(data)

    return data


def save_progress(progress: Dict[str, Any]) -> None:
    """
    Save progress to progress.json.
    """

    validate_progress(progress)

    with PROGRESS_FILE.open("w", encoding="utf-8") as file:
        json.dump(progress, file, indent=4)


def validate_progress(progress: Dict[str, Any]) -> None:
    """
    Validate required fields and values.
    """

    required = [
        "current_day",
        "total_days",
        "current_topic",
        "last_release",
    ]

    for key in required:
        if key not in progress:
            raise ProgressError(f"Missing field: {key}")

    if not isinstance(progress["current_day"], int):
        raise ProgressError("current_day must be an integer")

    if not isinstance(progress["total_days"], int):
        raise ProgressError("total_days must be an integer")

    if progress["current_day"] < 0:
        raise ProgressError("current_day cannot be negative")

    if progress["current_day"] > progress["total_days"]:
        raise ProgressError("current_day exceeds total_days")


def initialize_progress() -> None:
    """
    Create progress.json using default values if it does not exist.
    """

    if not PROGRESS_FILE.exists():
        save_progress(DEFAULT_PROGRESS.copy())


def get_current_day() -> int:
    """
    Return current published day.
    """

    return load_progress()["current_day"]


def get_total_days() -> int:
    """
    Return total planned lessons.
    """

    return load_progress()["total_days"]


def get_current_topic() -> str:
    """
    Return current topic.
    """

    return load_progress()["current_topic"]


def set_current_topic(topic: str) -> None:
    """
    Update current topic.
    """

    progress = load_progress()
    progress["current_topic"] = topic
    save_progress(progress)


def set_last_release(date: str) -> None:
    """
    Update last release date.
    """

    progress = load_progress()
    progress["last_release"] = date
    save_progress(progress)


def increment_day() -> int:
    """
    Increment the current day by one.

    Returns:
        New current day.

    Raises:
        ProgressError if all lessons have already been published.
    """

    progress = load_progress()

    if progress["current_day"] >= progress["total_days"]:
        raise ProgressError(
            "All lessons have already been published."
        )

    progress["current_day"] += 1

    save_progress(progress)

    return progress["current_day"]


if __name__ == "__main__":
    initialize_progress()

    progress = load_progress()

    print(
        f"Day {progress['current_day']} of {progress['total_days']}"
    )
