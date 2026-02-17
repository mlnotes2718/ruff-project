# Ruff + VSCode Cheat Sheet

## 1️⃣ Project Setup
```
ruff-project/
    .vscode/
        settings.json       ← VSCode editor settings
    pyproject.toml          ← Ruff configuration
    test.py                 ← your Python code
```

**pyproject.toml (minimal example)**
```toml
[tool.ruff]
line-length = 88
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "UP"]

[tool.ruff.format]
quote-style = "double"
```

**.vscode/settings.json (auto-fix & format on save)**
```json
{
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.fixAll.ruff": true
  },
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  }
}
```

## 2️⃣ Commands (CLI)
- **Check lint rules** (find issues):
```bash
ruff check .
```

- **Check and fix lint issues** (unused imports, pyflakes issues, import sorting):
```bash
ruff check . --fix
```

- **Format code** (spacing, quotes, indentation):
```bash
ruff format .
```

- **Check + Fix → then Format** (full cleanup workflow):
```bash
ruff check . --fix
ruff format .
```

## 3️⃣ Workflow for ML Projects
| Step | What it does | Command / VSCode |
|------|-------------|----------------|
| 1 | Check/fix unused imports, undefined vars, outdated syntax | `ruff check . --fix` or save in VSCode |
| 2 | Normalize spacing, quotes, indentation | `ruff format .` or save in VSCode |
| 3 | Work in notebook | Ignore lint, just experiment |
| 4 | Move notebook code → `.py` | Run above commands before committing |

## 4️⃣ Quick Mental Models
- `check` → **surgery** (structural / semantic fixes)
- `format` → **g