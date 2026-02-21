In 2026, Python type hinting has moved from an "extra" to a professional requirement. Below is a comprehensive guide to mastering type hints and Mypy using modern tools like **uv** and **Conda**.

---

## Part 1: The Type Hinting Guide (Modern Syntax)

Since Python 3.10+, typing has become much cleaner. You no longer need to import `List` or `Dict` for basic collections.

### 1. Basic & Collection Types

```python
# Simple Types
age: int = 25
price: float = 19.99
is_active: bool = True

# Collections (Modern 3.10+ syntax)
names: list[str] = ["Alice", "Bob"]
user_scores: dict[str, int] = {"Alice": 95}
coordinates: tuple[int, int] = (10, 20)

```

### 2. Unions and "Optional" Values

The pipe operator (`|`) has replaced the bulky `Union` and `Optional` imports.

```python
# "Optional" (either a string or None)
middle_name: str | None = None

# "Union" (can be an int OR a float)
def calculate_tax(amount: int | float) -> float:
    return amount * 0.15

```

### 3. Structural Types (TypedDict & Literal)

Use these when you need more precision than just `dict` or `str`.

```python
from typing import TypedDict, Literal

class User(TypedDict):
    username: str
    role: Literal["admin", "user", "guest"]

new_user: User = {"username": "alice", "role": "admin"}

def greet(name: str, count: int = 1) -> list[str]:
    return [f"Hello {name}"] * count
```

### 4. Functions
Always annotate your arguments and the return type (->).

```python
def greet(name: str, count: int = 1) -> list[str]:
    return [f"Hello {name}"] * count
```


### 5. Type Hinting Cheat Sheet (Modern Python)

Python 3.10+ uses cleaner syntax for collections and multiple types.

* **Collections:** `list[int]`, `dict[str, float]`, `set[str]`
* **Unions (Either/Or):** `int | float` (replaces `Union[int, float]`)
* **Optional (Value or None):** `str | None` (replaces `Optional[str]`)
* **Specific Strings/Numbers:** `Literal["admin", "user"]`
* **DataFrames:** `pd.DataFrame` (requires `pandas-stubs`)

---

## Part 2: Mypy Setup & Common Stubs

### 1. Installation

| Tool | Installation Command | Run Command |
| --- | --- | --- |
| **uv** | `uv add --dev mypy` | `uv run mypy .` |
| **Conda** | `conda install -c conda-forge mypy` | `mypy your_script.py` |

Run without installing (ad-hoc):
```bash
uvx mypy script.py
```

### 2. Commonly Used Stubs

Many libraries don't ship with types. You must install "stubs" (packages ending in `-stubs` or starting with `types-`).

**Data Science & General Stubs:**

Mypy needs "stubs" to understand third-party libraries. If you get `Library stubs not installed`, use these commands:

| Library | **uv** Install | **Conda** Install |
| --- | --- | --- |
| **Pandas** | `uv add --dev pandas-stubs` | `conda install -c conda-forge pandas-stubs` |
| **Requests** | `uv add --dev types-requests` | `conda install -c conda-forge types-requests` |
| **PyYAML** | `uv add --dev types-PyYAML` | `conda install -c conda-forge types-pyyaml` |
| **Boto3** | `uv add --dev boto3-stubs` | `conda install -c conda-forge boto3-stubs` |

**How to Install Stubs:**

* **Using uv:**
```bash
uv add --dev pandas-stubs types-requests types-PyYAML

```


* **Using Conda:**
```bash
conda install -c conda-forge pandas-stubs types-requests types-pyyaml

```



---

## Part 3: Essential Mypy CLI Commands

Running `mypy script.py` is just the start. Use these flags to gain more control:

### 1. The "Golden" Flag: `--strict`

This is the "pro mode." It enables nearly all of Mypy's check flags, forcing you to annotate every function and disallowing `Any`.

```bash
mypy --strict .

```

### 2. Automatic Stub Helper

If you have many missing imports, let Mypy find the stubs for you:

```bash
mypy --install-types --non-interactive

```

### 3. Advanced CLI Commands & Flags

* **`--strict`**: The "no-nonsense" mode. It turns on every strictness flag, requiring annotations for all functions and banning `Any`. Use this for new projects.
* **`--ignore-missing-imports`**: Stops Mypy from complaining about libraries that don't have stubs.
* **`--show-error-codes`**: Highly recommended. It shows the specific error name (e.g., `[attr-defined]`), making it easier to ignore specific lines using `# type: ignore[error-code]`.
* **`--check-untyped-defs`**: Forces Mypy to look inside functions even if you haven't added a return type hint yet.
* **`--pretty`**: Makes the output more readable with color-coding and clear markers.
* **`--exclude`**: Skip specific folders (like migrations or tests).
```bash
mypy . --exclude "tests/"

```



---

## Part 4: The `pyproject.toml` Configuration

Instead of typing long commands, save your preferences in your project root. Mypy will pick these up automatically.

```toml
[tool.mypy]
python_version = "3.12"
strict = true
warn_return_any = true
warn_unused_configs = true
show_error_codes = true
ignore_missing_imports = true

# Overrides for specific parts of your project
[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false  # Relax rules for test files

```

## Summary Comparison

| Feature | Standard Python | With Mypy |
| --- | --- | --- |
| **Error Detection** | At runtime (when code runs) | Before execution (static) |
| **Refactoring** | Risky (might break things) | Safe (Mypy flags every break) |
| **Documentation** | Comments/Docstrings | Self-documenting code |
| **Speed** | No impact | Faster development, slower CI check |










---







