"""
utils.py

Common utility functions shared across the Python 365 automation engine.
"""

from __future__ import annotations

import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


def ensure_directory(path: Path) -> None:
    """Create a directory if it doesn't already exist."""
    path.mkdir(parents=True, exist_ok=True)


def copy_directory(source: Path, destination: Path) -> None:
    """
    Copy an entire directory recursively.

    Existing destination will be replaced.
    """
    if destination.exists():
        shutil.rmtree(destination)

    shutil.copytree(source, destination)


def read_json(path: Path) -> dict[str, Any]:
    """Read JSON from a file."""
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def write_json(path: Path, data: dict[str, Any]) -> None:
    """Write JSON to a file."""
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_text(path: Path) -> str:
    """Read UTF-8 text from a file."""
    return path.read_text(encoding="utf-8")


def write_text(path: Path, content: str) -> None:
    """Write UTF-8 text to a file."""
    path.write_text(content, encoding="utf-8")


def current_date() -> str:
    """Return today's date."""
    return datetime.now().strftime("%Y-%m-%d")


def current_datetime() -> str:
    """Return current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def day_folder(day: int) -> str:
    """
    Convert a day number into folder format.

    Example:
        1 -> Day001
        27 -> Day027
    """
    return f"Day{day:03d}"


def progress_bar(current: int, total: int, width: int = 20) -> str:
    """
    Generate a Unicode progress bar.

    Example:
    ███████░░░░░░░░░░░
    """
    filled = int((current / total) * width)
    return "█" * filled + "░" * (width - filled)


def percentage(current: int, total: int) -> float:
    """Return completion percentage."""
    return round((current / total) * 100, 2)


def safe_delete(path: Path) -> None:
    """Delete file or directory if it exists."""
    if not path.exists():
        return

    if path.is_dir():
        shutil.rmtree(path)
    else:
        path.unlink()
