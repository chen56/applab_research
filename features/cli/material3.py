#!/usr/bin/env python3
"""
Material 3 × Terminal (Rich) reference implementation

Layer model (CLI-optimized):
1. Color Tokens (Material 3 standard roles)
2. UX Semantics (mapped, NOT colors)

Authoritative rule:
- Only `error` is a semantic color
- success / warning / info are UX semantics mapped to roles

log ref:
- <https://uptrace.dev/get/opentelemetry-python/logs>
"""

from typing import Dict, Literal
from rich_.console import Console
from rich_.theme import Theme
from rich_.style import Style


# ----------------------------------------------------------------------
# Layer 1: Material 3 Color Tokens (Design System Layer)
# ----------------------------------------------------------------------

M3Token = Literal[
    "primary",
    "on_primary",
    "secondary",
    "on_secondary",
    "tertiary",
    "on_tertiary",
    "error",
    "on_error",
    "surface",
    "on_surface",
    "surface_variant",
    "on_surface_variant",
    "outline",
]


class M3ColorTokens:
    """
    Strict Material 3 color tokens (Dark mode, standard contrast).
    These are NOT UX semantics.
    """

    def __init__(self):
        self.colors: Dict[M3Token, str] = {
            "primary": "#D0BCFF",
            "on_primary": "#381E72",

            "secondary": "#CCC2DC",
            "on_secondary": "#332D41",

            "tertiary": "#EFB8C8",
            "on_tertiary": "#492532",

            "error": "#F2B8B5",
            "on_error": "#601410",

            "surface": "#1C1B1F",
            "on_surface": "#E6E1E5",

            "surface_variant": "#49454F",
            "on_surface_variant": "#CAC4D0",

            "outline": "#938F99",
        }

    def to_rich_theme(self) -> Theme:
        """
        Convert color tokens into Rich styles.
        Names are token-based, not semantic.
        """
        c = self.colors
        return Theme({
            "primary": Style(color=c["on_primary"], bgcolor=c["primary"], bold=True),
            "secondary": Style(color=c["on_secondary"], bgcolor=c["secondary"]),
            "tertiary": Style(color=c["on_tertiary"], bgcolor=c["tertiary"]),
            "error": Style(color=c["on_error"], bgcolor=c["error"], bold=True),

            "surface": Style(color=c["on_surface"], bgcolor=c["surface"]),
            "surface_variant": Style(color=c["on_surface_variant"], bgcolor=c["surface_variant"]),
            "outline": Style(color=c["outline"]),
            "text": Style(color=c["on_surface"]),
        })


# ----------------------------------------------------------------------
# Layer 2: UX Semantics (Product Layer, NOT colors)
# ----------------------------------------------------------------------

UXSemantic = Literal["success", "warning", "info", "error", "neutral"]

class UXSemanticMapper:
    """
    Maps UX semantics to Material 3 color roles.

    This is policy, NOT design system.
    """

    MAP: Dict[UXSemantic, str] = {
        # No semantic color in M3 → mapped roles
        "success": "primary",
        "warning": "tertiary",
        "info": "surface_variant",
        "neutral": "surface",

        # The only true semantic color in M3
        "error": "error",
    }

    PREFIX: Dict[UXSemantic, str] = {
        "success": "[OK]",
        "warning": "[WARN]",
        "info": "[INFO]",
        "neutral": "[*]",
        "error": "[ERROR]",
    }

    @classmethod
    def style_for(cls, semantic: UXSemantic) -> str:
        return cls.MAP[semantic]

    @classmethod
    def prefix_for(cls, semantic: UXSemantic) -> str:
        return cls.PREFIX[semantic]


# ----------------------------------------------------------------------
# CLI Output Helper (What you actually use)
# ----------------------------------------------------------------------

class M3Console:
    def __init__(self):
        tokens = M3ColorTokens()
        self.console = Console(theme=tokens.to_rich_theme())

    def print(self, semantic: UXSemantic, message: str):
        style = UXSemanticMapper.style_for(semantic)
        prefix = UXSemanticMapper.prefix_for(semantic)
        self.console.print(f"[{style}]{prefix}[/{style}] {message}")


# ----------------------------------------------------------------------
# Demo / Entry point
# ----------------------------------------------------------------------

def main():
    cli = M3Console()

    cli.print("success", "Project initialized successfully")
    cli.print("info", "Using cached credentials")
    cli.print("warning", "Quota is approaching its limit")
    cli.print("neutral", "Waiting for user input")
    cli.print("error", "Failed to create cloud resource")


if __name__ == "__main__":
    main()
