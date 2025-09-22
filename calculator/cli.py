"""Simple REPL for the calculator.

Commands:
  add <a> <b>
  sub <a> <b>
  mul <a> <b>
  div <a> <b>
  quit

Parses a and b as floats and prints the result or error messages.
"""
from __future__ import annotations

from calculator import core


def repl() -> None:
    """Run a simple read-eval-print loop until the user quits."""
    print("Calculator REPL — commands: add|sub|mul|div|quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not raw:
            continue

        parts = raw.split()
        cmd = parts[0].lower()
        if cmd in ("q", "quit", "exit"):
            break

        if len(parts) != 3:
            print("Usage: <cmd> <a> <b> — e.g. 'add 1 2'")
            continue

        _, a_s, b_s = parts
        try:
            a = float(a_s)
            b = float(b_s)
        except ValueError:
            print("Invalid numbers. Please enter numeric values for a and b.")
            continue

        try:
            if cmd == "add":
                res = core.add(a, b)
            elif cmd in ("sub", "subtract"):
                res = core.subtract(a, b)
            elif cmd in ("mul", "multiply"):
                res = core.multiply(a, b)
            elif cmd in ("div", "divide"):
                res = core.divide(a, b)
            else:
                print(f"Unknown command: {cmd}")
                continue
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")
        else:
            print(res)


if __name__ == "__main__":
    repl()
