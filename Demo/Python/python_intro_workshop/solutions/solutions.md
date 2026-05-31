Solutions — Python Intro Workshop (short)

1. hello.py
```python
print("Hello, world")
```

2. Basics
```python
name = "Alex"
age = 30
balance = 12.5
print(name, age, balance)
```

Greet user:
```python
name = input("Your name: ")
print(f"Hello, {name}!")
```

3. Even or odd
```python
try:
    n = int(input("Number: "))
    print("Even" if n % 2 == 0 else "Odd")
except ValueError:
    print("Please enter an integer.")
```

4. Function examples
```python
def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b
```

5. Collections
```python
foods = ["pizza", "salad", "sushi"]
for i, f in enumerate(foods, 1):
    print(i, f)

contact = {"name": "Alex", "phone": "+123456"}
print(contact["phone"])
```

6. Error handling: see earlier even/odd example.

7. Practical: Use `src/expense_tracker.py` and follow prompts to add/list/remove expenses.