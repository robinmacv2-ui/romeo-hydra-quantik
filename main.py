#!/usr/bin/env python3
"""ROMEO-HYDRA QUANTIK — public evaluation door (stdlib only)."""

from pathlib import Path

HUB = "https://github.com/robinmacv2-ui/romeo-hydra-master-repository-hub"
GENESIS = "https://github.com/robinmacv2-ui/hydra-genesis-zero"
CHECKLIST = f"{HUB}/blob/main/JURY_CHECKLIST.md"

def main() -> None:
    print("ROMEO-HYDRA QUANTIK")
    print("Public evaluation door · offline fail-closed ecosystem")
    print("Core claim path = Python 3.11 stdlib only")
    print()
    print("=== Jury route A (product surface, recommended) ===")
    print(f"  git clone --depth 1 {HUB}.git")
    print("  cd romeo-hydra-master-repository-hub")
    print("  python3 -m venv .venv && source .venv/bin/activate")
    print("  pip install -e .          # ZERO third-party packages")
    print("  python main.py")
    print('  python -m romeo_agent -c "status ::"')
    print('  python -m romeo_agent -c "help ::"')
    print()
    print("=== Jury route B (pure kernel) ===")
    print(f"  git clone --depth 1 {GENESIS}.git")
    print("  cd hydra-genesis-zero && python3 main.py")
    print()
    print("Full checklist:")
    print(f"  {CHECKLIST}")
    print()
    print("Non-claims: not CNBV-certified · not production banking · not an LLM")
    print("Base path:", Path(__file__).parent.resolve())

if __name__ == "__main__":
    main()
