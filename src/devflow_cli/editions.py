"""Canonical metadata for the two independently maintained DevFlow editions."""

from typing import Dict, Tuple


DEFAULT_EDITION = "classic"
HOSTS: Tuple[str, ...] = ("codebuddy", "codex", "cursor", "claude")
HOST_LABELS = {
    "codebuddy": "CodeBuddy",
    "codex": "Codex",
    "cursor": "Cursor",
    "claude": "Claude Code",
}

EDITION_SPECS: Dict[str, dict] = {
    "portable": {
        "description": "Agent Skills based portable workflow",
        "source_roots": ("skills/",),
        "entrypoints": {
            "codebuddy": "/devflow",
            "codex": "$devflow",
            "cursor": "/devflow",
            "claude": "/devflow",
        },
    },
    "classic": {
        "description": "Full host-native workflow derived from .codebuddy behavior",
        "source_roots": (".codebuddy/", ".codex/", ".cursor/", ".claude/"),
        "entrypoints": {
            "codebuddy": "/start-devflow",
            "codex": "$devflow-codex",
            "cursor": "/start-devflow",
            "claude": "/start-devflow",
        },
    },
}

EDITIONS: Tuple[str, ...] = tuple(EDITION_SPECS)


def spec(edition: str) -> dict:
    return EDITION_SPECS[edition]


def source_for(edition: str, host: str) -> str:
    if edition == "classic":
        return f".{host}/"
    return "skills/"


def entrypoint_for(edition: str, host: str) -> str:
    return str(spec(edition)["entrypoints"][host])


def host_label(host: str) -> str:
    return str(HOST_LABELS[host])
