from __future__ import annotations

import pathlib
import random
import sys

import typing
from typing import (
    AbstractSet,
    Container,
    FrozenSet,
    Iterable,
    Tuple,
)

import gidgethub.abc
import gidgethub.httpx
import gidgethub.actions
import httpx
import trio


def should_update_eslintignore(
    files: Iterable[str], eslintignore: Iterable[str]
) -> bool:
    """Check if any of the file paths are in the list of paths in the .eslintignore."""
    return any(file in files for file in eslintignore)


def get_list_of_files(gh: gidgethub.abc.GitHubAPI) -> Iterable[str]:
    """Get the list of files modified in this PR."""


async def main(token: str):
    event = gidgethub.actions.event()
    print("do something")


if __name__ == "__main__":
    trio.run(main, sys.argv[1])