"""
POC_U1B2 - Unit 01 - Functions - Block 02
Pair Programming Lab: Function Builder Pack
Names: Kaliel Williamson  ______________________  (______________________)

Instructions:
- Complete each TODO.
- Run after each function to test.
- Use parameters + return whenever possible.
- Avoid global variables.
- Prefer small, single-purpose functions.

Roles (switch halfway)
Driver: types, runs the code, shares screen/keyboard
Navigator: reads instructions, watches for mistakes, explains “why”

Suggested Timing (40 minutes)
0–5 min: Setup + run once (expect failures)
5–20 min: Parts A–B
20 min: Switch Driver/Navigator
20–35 min: Parts C–D
35–40 min: Part E + cleanup (all tests pass)

Each person will turn in a complete copy. Make sure all work is present for both students.
When finished turn this in on GitHub and Canvas.
This portion is worth 15 points.
"""

print("\n=== POC_U1B2 PAIR LAB: Function Builder Pack ===\n")


# ============================================================
# PART A: Warm-up (return values, not prints)
# ============================================================

def is_even(n):
    """Return True if n is even, otherwise False."""
    return n % 2 == 0

    raise NotImplementedError


def average(a, b):
    """Return the average of a and b."""
    return (a + b) / 2

    raise NotImplementedError


def seconds_to_minutes(seconds):
    """
    Convert seconds to minutes as a float.
    Example: 90 seconds -> 1.5 minutes
    """
    return seconds / 60


# ============================================================
# PART B: Positional vs Keyword + Defaults
# ============================================================

def greet(name, punctuation="!"):
    """
    Return a greeting string.
    greet("Ada") -> "Hello, Ada!"
    greet("Ada", "?") -> "Hello, Ada?"
    """
    return f"Hello, {name}{punctuation}"

    raise NotImplementedError


def percent_of(part, whole, digits=1):
    """
    Return a percentage string rounded to 'digits' decimals.
    percent_of(1, 4) -> "25.0%"
    percent_of(1, 4, digits=0) -> "25%"
    """
    if whole == 0:
        return "0%"
    percentage = (part / whole) * 100
    rounded = round(percentage, digits)
    # Format without trailing decimals if digits=0
    if digits == 0:
        return f"{int(rounded)}%"
    else:
        return f"{rounded}%"

    raise NotImplementedError


# ============================================================
# PART C: Return vs Print (build strings)
# ============================================================

def line_total(quantity, price_each):
    """Return quantity * price_each."""
    return quantity * price_each

    raise NotImplementedError


def receipt_line(item, quantity, price_each):
    """
    Return a formatted receipt line string.
    Example: receipt_line("Soda", 2, 1.5) -> "Soda x2 = $3.00"
    """
    total = line_total(quantity, price_each)
    return f"{item} x{quantity} = ${total:.2f}"

    raise NotImplementedError


# ============================================================
# PART D: Scope + Side Effects (mutating vs non-mutating)
# ============================================================

def add_item_mutating(items, new_item):
    """
    Add new_item to the existing list 'items' (mutates it).
    Return None.
    """
    items.append(new_item)
    return None

    raise NotImplementedError


def add_item_copy(items, new_item):
    """
    Return a NEW list that contains all items plus new_item.
    Do NOT mutate the original list.
    """
    return items + [new_item]

    raise NotImplementedError


# ============================================================
# PART E: Mini-Challenge (combine your functions)
# ============================================================

def build_receipt(items):
    """
    items is a list of tuples: (name, quantity, price_each)

    Return a multi-line receipt string that includes:
    - One receipt_line per item
    - A final TOTAL line formatted like: "TOTAL = $X.XX"

    Example return:

    Soda x2 = $3.00
    Chips x1 = $2.25
    TOTAL = $5.25
    """
    lines = []
    total_cost = 0.0

    for name, quantity, price_each in items:
        lines.append(receipt_line(name, quantity, price_each))
        total_cost += line_total(quantity, price_each)

    lines.append(f"TOTAL = ${total_cost:.2f}")

    return "\n".join(lines)

    raise NotImplementedError


# ============================================================
# TESTS (Run often. Start by doing Part A and uncommenting.)
# ============================================================

print("=== TESTS (Uncomment as you finish each part) ===\n")

# --- Part A ---
assert is_even(2) is True
assert is_even(7) is False
assert average(10, 20) == 15
assert seconds_to_minutes(90) == 1.5
def is_even(n):
    return n % 2 == 0

def average(a, b):
    return (a + b) / 2

def seconds_to_minutes(seconds):
    return seconds / 60


# --- Part B ---
assert greet("Ada") == "Hello, Ada!"
assert greet("Ada", "?") == "Hello, Ada?"
assert percent_of(1, 4) == "25.0%"
assert percent_of(1, 4, digits=0) == "25%"
def greet(name, punctuation='!'):
    return f"Hello, {name}{punctuation}"

def percent_of(part, whole, digits=1):
    percentage = (part / whole) * 100
    if digits == 0:
        return f"{int(round(percentage))}%"
    else:
        return f"{round(percentage, digits)}%"

# --- Part C ---
assert line_total(3, 2.0) == 6.0
assert receipt_line("Soda", 2, 1.5) == "Soda x2 = $3.00"
def line_total(quantity, price):
    return quantity * price

def receipt_line(item, quantity, price):
    total = line_total(quantity, price)
    return f"{item} x{quantity} = ${total:.2f}"



# --- Part D ---
original = ["apple"]
add_item_mutating(original, "banana")
assert original == ["apple", "banana"]

original2 = ["apple"]
copy_list = add_item_copy(original2, "banana")
assert original2 == ["apple"]            # original unchanged
assert copy_list == ["apple", "banana"]  # new list returned
def add_item_mutating(lst, item):
    lst.append(item)

def add_item_copy(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list


# --- Part E ---
cart = [("Soda", 2, 1.5), ("Chips", 1, 2.25)]
expected = "Soda x2 = $3.00\nChips x1 = $2.25\nTOTAL = $5.25"
assert build_receipt(cart) == expected
def build_receipt(cart):
    lines = []
    total = 0
    for item, quantity, price in cart:
        line_total = quantity * price
        total += line_total
        lines.append(f"{item} x{quantity} = ${line_total:.2f}")
    lines.append(f"TOTAL = ${total:.2f}")
    return "\n".join(lines)


print("When all asserts pass: push to GitHub, submit to Canvas. ✅")
