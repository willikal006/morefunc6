"""
POC_U1B2 - Unit 01 - Functions - Block 02 - Functions Deep Dive (Guided Notes)
Name: ______________________

STUDENTS:
- Fill in the blanks by writing answers in COMMENTS.
- Complete the TODO code.
- Run this file often to see what happens.

Timing (20 minutes total)
0–3 min: Vocabulary + purpose
3–8 min: Parameters vs arguments (positional + keyword)
8–12 min: return vs print (+ None)
12–16 min: Default parameters + optional arguments
16–20 min: Scope + quick tests (assert)

"""

print("\n=== POC_U1B2 GUIDED NOTES: Functions Deep Dive ===\n")


# ============================================================
# 1) VOCAB + BIG IDEAS (Fill in blanks in COMMENTS)
# ============================================================

# A function is a named block of code that can be reused.
# A parameter is variable used at the start of the function.
# An argument is value given to the function when called.
# The return value is given back to where you called the function.
# If a function has no return statement, it returns none.
# A local variable is a variable that exists only in the function block.
# Scope means where does a variable exist.
# A "side effect" is when a function does something outside the code.

# BONUS: What is the difference between "print" and "return"?
# print: is a side effect
# return: is not a side effect


# ============================================================
# 2) PARAMETERS vs ARGUMENTS (positional + keyword)
# ============================================================

def add(a, b):
    """Return the sum of a and b."""
    return a + b

print("add(2, 5) ->", add(2, 5))

# Positional arguments: matched by position
print("add(10, 3) ->", add(10, 3))

# Keyword arguments: matched by parameter name
print("add(a=10, b=3) ->", add(a=10, b=3))
print("add(b=3, a=10) ->", add(b=3, a=10))


# ============================================================
# 3) RETURN vs PRINT (+ None)
# ============================================================

def say_hello(name):
    # This function PRINTS, but does not RETURN a value.
    print(f"Hello, {name}!")

result = say_hello("Ada")
print("result after calling say_hello('Ada') is ->", result)  # should be None


def make_hello(name):
    # This function RETURNS a string instead of printing it.
    return f"Hello, {name}!"

result2 = make_hello("Grace")
print("result2 after calling make_hello('Grace') is ->", result2)


# ============================================================
# 4) DEFAULT PARAMETERS (optional arguments)
# ============================================================

def power(base, exp=2):
    """Return base raised to exp. Default exp is 2."""
    return base ** exp

print("power(5) ->", power(5))          # 5^2
print("power(5, 3) ->", power(5, 3))    # 5^3
print("power(base=2, exp=5) ->", power(base=2, exp=5))


# ============================================================
# 5) MULTIPLE RETURNS (returning a tuple)
# ============================================================

def quotient_remainder(a, b):
    """Return (quotient, remainder) for integer division."""
    q = a // b
    r = a % b
    return q, r

q, r = quotient_remainder(17, 5)
print("quotient_remainder(17, 5) ->", (q, r))


# ============================================================
# 6) SCOPE (local vs global) + WHY WE AVOID "global"
# ============================================================

score = 10  # global variable (defined outside any function)

def add_points(points):
    # This score is LOCAL. It does NOT change the global score.
    score = 0
    score = score + points
    return score

print("\nGlobal score BEFORE:", score)
local_score = add_points(5)
print("Value returned from add_points(5):", local_score)
print("Global score AFTER:", score)

# Key idea:
# - A variable created inside a function is usually LOCAL to that function.
# - Changing a local variable does not change a global variable with the same name.


# ============================================================
# 7) QUICK PRACTICE (TODOs) + ASSERT TESTS
# ============================================================

def repeat_text(text, times):
    """


   def repeat_text

    def clamp(n, low, high)
    if n>=low and n<=high:
    return high
    elif n>=low and n<=high:
    return low
    return n



def clamp(n, low, high):
    """
    TODO:
    Return n, but limited to the inclusive range [low, high].
    clamp(5, 0, 10) -> 5
    clamp(-2, 0, 10) -> 0
    clamp(999, 0, 10) -> 10
    """
    raise NotImplementedError


def format_full_name(first, last, middle=""):
    """
    TODO:
    Return a properly spaced full name.
    If middle is "", return "First Last"
    Otherwise return "First Middle Last"
    """
    raise NotImplementedError


print("\n=== TODO TESTS (Expect failures until you finish TODOs) ===")

# Uncomment as you complete them:
# assert repeat_text("ha", 3) == "hahaha"
# assert repeat_text("x", 1) == "x"
# assert clamp(5, 0, 10) == 5
# assert clamp(-2, 0, 10) == 0
# assert clamp(999, 0, 10) == 10
# assert format_full_name("Ada", "Lovelace") == "Ada Lovelace"
# assert format_full_name("James", "Kirk", "Tiberius") == "James Tiberius Kirk"

print("When all asserts pass, you’re officially dangerous. ✅")
