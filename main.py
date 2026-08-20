#!/usr/bin/env python3
"""ROMEO-HYDRA QUANTIK — public entrypoint (stdlib only)."""

from pathlib import Path

def main() -> None:
    print("ROMEO-HYDRA QUANTIK")
    print("Public evaluation entrypoint")
    print("Core path = pure Python 3.11 stdlib")
    print()
    print("Recommended next step for jury:")
    print("  git clone https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub.git")
    print("  cd romeo-hydra-master-repository-hub")
    print("  python3 -m venv .venv && source .venv/bin/activate")
    print("  pip install -e .")
    print("  python main.py")
    print()
    print("Full checklist:")
    print("  https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub/blob/main/JURY_CHECKLIST.md")
    print()
    print("Base path:", Path(__file__).parent.resolve())

if __name__ == "__main__":
    main()
