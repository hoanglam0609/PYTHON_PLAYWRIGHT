"""Personal Expense Tracker - Beginner-friendly CLI app

Features:
- Add expense (amount, category, note)
- List expenses
- Show total
- Remove expense
- Save/load to JSON (simple persistence)

Run: python3 src/expense_tracker.py
"""
from __future__ import annotations

import json
import os
from dataclasses import dataclass, asdict
from typing import List

DATA_FILE = os.path.join(os.path.dirname(__file__), "expenses.json")


@dataclass
class Expense:
    amount: float
    category: str
    note: str


def load_expenses(path: str = DATA_FILE) -> List[Expense]:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            raw = json.load(f)
        return [Expense(**r) for r in raw]
    except Exception:
        return []


def save_expenses(expenses: List[Expense], path: str = DATA_FILE) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([asdict(e) for e in expenses], f, indent=2, ensure_ascii=False)


def add_expense(expenses: List[Expense]) -> None:
    try:
        amt = float(input("Amount (e.g. 12.50): ").strip())
    except ValueError:
        print("Invalid amount. Try again.")
        return
    cat = input("Category (e.g. food, transport): ").strip() or "uncategorized"
    note = input("Note (optional): ").strip()
    expenses.append(Expense(amount=amt, category=cat, note=note))
    save_expenses(expenses)
    print("Expense added.")


def list_expenses(expenses: List[Expense]) -> None:
    if not expenses:
        print("No expenses recorded.")
        return
    for i, e in enumerate(expenses, start=1):
        print(f"{i}. {e.category}: {e.amount:.2f} — {e.note}")


def total_expenses(expenses: List[Expense]) -> None:
    total = sum(e.amount for e in expenses)
    print(f"Total expenses: {total:.2f}")


def remove_expense(expenses: List[Expense]) -> None:
    list_expenses(expenses)
    if not expenses:
        return
    try:
        idx = int(input("Enter expense number to remove: ").strip())
        if 1 <= idx <= len(expenses):
            removed = expenses.pop(idx - 1)
            save_expenses(expenses)
            print(f"Removed: {removed.category} {removed.amount:.2f} — {removed.note}")
        else:
            print("Number out of range.")
    except ValueError:
        print("Invalid number.")


def main() -> None:
    expenses = load_expenses()
    actions = {
        "1": ("Add expense", add_expense),
        "2": ("List expenses", list_expenses),
        "3": ("Show total", total_expenses),
        "4": ("Remove expense", remove_expense),
        "5": ("Quit", None),
    }

    while True:
        print("\nPersonal Expense Tracker")
        for k, (label, _) in actions.items():
            print(f"{k}. {label}")
        choice = input("Choose an action: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if not action:
            print("Unknown option — try again.")
            continue
        _, func = action
        try:
            func(expenses)
        except Exception as exc:
            print("An error occurred:", exc)


if __name__ == "__main__":
    main()
