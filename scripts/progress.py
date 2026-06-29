"""
progress.py

Handles reading, validating, and updating the project's progress.json file.

This module is the single source of truth for the automation engine.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

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


def validate_progress(progress: dict[str, Any]) -> None:
    """
    Validate the structure and values of progress.json.
    """

    required_fields = [
        "current_day",
        "total_days",
        "current_topic",
        "last_release",
    ]

    for field in required_fields:
        if field not in progress:
            raise ProgressError(f"Missing required field: {field}")

    if not isinstance(progress["current_day"], int):
        raise ProgressError("current_day must be an integer.")

    if not isinstance(progress["total_days"], int):
        raise ProgressError("total_days must be an integer.")

    if not isinstance(progress["current_topic"], str):
        raise ProgressError("current_topic must be a string.")

    if (
        progress["last_release"] is not None
        and not isinstance(progress["last_release"], str)
    ):
        raise ProgressError("last_release must be a string or null.")

    if progress["current_day"] < 0:
        raise ProgressError("current_day cannot be negative.")

    if progress["current_day"] > progress["total_days"]:
        raise ProgressError("current_day cannot exceed total_days.")


def initialize_progress() -> None:
    """
    Create progress.json if it does not exist.
    """

    if PROGRESS_FILE.exists():
        return

    save_progress(DEFAULT_PROGRESS.copy())


def load_progress() -> dict[str, Any]:
    """
    Load and validate progress.json.
    """

    initialize_progress()

    with PROGRESS_FILE.open("r", encoding="utf-8") as file:
        progress = json.load(file)

    validate_progress(progress)

    return progress


def save_progress(progress: dict[str, Any]) -> None:
    """
    Save progress.json.
    """

    validate_progress(progress)

    with PROGRESS_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            progress,
            file,
            indent=4,
            ensure_ascii=False,
        )
        file.write("\n")


def get_current_day() -> int:
    return load_progress()["current_day"]


def get_total_days() -> int:
    return load_progress()["total_days"]


def get_current_topic() -> str:
    return load_progress()["current_topic"]


def get_last_release() -> str | None:
    return load_progress()["last_release"]


def set_current_day(day: int) -> None:
    progress = load_progress()
    progress["current_day"] = day
    save_progress(progress)


def set_current_topic(topic: str) -> None:
    progress = load_progress()
    progress["current_topic"] = topic
    save_progress(progress)


def set_last_release(date: str) -> None:
    progress = load_progress()
    progress["last_release"] = date
    save_progress(progress)


def increment_day() -> int:
    """
    Increase current_day by one.

    Returns:
        Updated day number.
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

    print("=" * 40)
    print("Python 365 Progress")
    print("=" * 40)
    print(f"Current Day   : {progress['current_day']}")
    print(f"Total Days    : {progress['total_days']}")
    print(f"Current Topic : {progress['current_topic']}")
    print(f"Last Release  : {progress['last_release']}")
