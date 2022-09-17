# type: ignore[attr-defined]
"""Compares text in a file to reference/glossary/key-items/dictionary file."""

import sys
from importlib import metadata as importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:
        return "unknown"


version: str = get_version()
