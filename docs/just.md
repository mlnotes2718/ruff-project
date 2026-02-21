In 2026, **Just** has become the "glue" that holds together complex Python workflows, especially when mixing tools like **Conda** and **uv**. Because `just` is written in Rust, it's cross-platform and extremely fast.

---

## 1. Installation Guide

For a professional workflow, you want `just` installed globally (so you can run it anywhere) rather than inside a specific virtual environment.

### Option A: Using Conda (Best for DS/ML)

If you already use Conda, install `just` into your `base` environment or via `conda-forge`. This ensures it's available as soon as you open your terminal.

```bash
# Install to your current environment
conda install -c conda-forge just

# Pro Tip: Use mamba for faster installation
mamba install -c conda-forge just

```

### Option B: Using uv (Best for DE/General)

`uv` has a dedicated "tool" interface designed exactly for things like `just`. This installs `just` into an isolated, managed location and adds it to your system PATH.

```bash
# The 'uv' way to install standalone tools
uv tool install just

# Verify installation
just --version

```

### Option C: OS-Specific (Alternative)

* **macOS:** `brew install just`
* **Windows:** `winget install casey.just` or `choco install just`

---

## 2. Configuring the `justfile` for Hybrid Environments

The power of `just` is that it can detect your environment. Below is a professional configuration that automatically switches between **uv** and **Conda** based on what's available in your project.

### Creating the `justfile`

Create a file named `justfile` (no extension) in your project root:

```just
# Set variables
project_name := "data-pipeline"

# Detect if we are using uv or conda
# This checks if uv.lock exists to prioritize uv
env_type := if path_exists("uv.lock") { "uv" } else { "conda" }

# Default task: list all commands
default:
    @just --list

# --- Core Commands ---

# Setup the environment
setup:
    @echo "Setting up using {{env_type}}..."
    @if [ "{{env_type}}" == "uv" ]; then \
        uv sync; \
    else \
        conda env create -f environment.yml; \
    fi

# Run Type Checking
typecheck:
    @echo "🛡️ Running Mypy..."
    @if [ "{{env_type}}" == "uv" ]; then \
        uv run mypy .; \
    else \
        mypy .; \
    fi

# Run Linting
lint:
    @echo "🔍 Running Ruff..."
    @if [ "{{env_type}}" == "uv" ]; then \
        uv run ruff check . --fix; \
    else \
        ruff check . --fix; \
    fi

# Run Tests
test *args:
    @echo "🧪 Running Pytest..."
    @if [ "{{env_type}}" == "uv" ]; then \
        uv run pytest {{args}}; \
    else \
        pytest {{args}}; \
    fi

```

---

## 3. Advanced Configuration Tips

### 1. Handling Windows vs. Unix

By default, `just` uses `sh`. If you are on Windows and don't have Git Bash, add this to the top of your `justfile` to use PowerShell:

```just
set shell := ["powershell.exe", "-c"]

```

### 2. Loading Environment Variables

`just` can automatically load your `.env` file for all recipes. This is perfect for Data Engineering credentials:

```just
set dotenv-load := true

```

### 3. Argument Passing

In the `test` recipe above, notice the `*args`. This allows you to pass flags directly through `just` to `pytest`:

* **Command:** `just test -v -k "login"`
* **Result:** Runs `uv run pytest -v -k "login"`

---

## 4. Summary of Commands

| Task | Command | Why use it? |
| --- | --- | --- |
| **List Tasks** | `just` | See your project's "menu". |
| **Full Check** | `just lint typecheck test` | Run your entire CI suite locally. |
| **New Task** | `just <task_name>` | Run any custom recipe you've added. |

**Would you like me to show you how to add a "Data Pipeline" recipe that handles downloading data from S3 before running your Mypy checks?**