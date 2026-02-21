# 🚀 Ruff in VS Code: The "No-TOML" Manual Guide

This guide is optimized for developers using **Auto Save** who want a fast, non-intrusive linting experience without creating extra configuration files.

---

## 🛠️ 1. Setup & Installation

1.  **Install Extension:** Open Extensions (`Ctrl+Shift+X`) and install **"Ruff"** by Astral Software.
2.  **Disable "On Save" Frustration:** Since you use Auto Save, prevent Ruff from jumping your cursor around by updating your `settings.json`:
    * Press `Ctrl+Shift+P`, type "Open User Settings (JSON)".
    * Ensure these keys are set:
    ```json
    {
      "files.autoSave": "afterDelay",
      "[python]": {
        "editor.formatOnSave": false,
        "editor.codeActionsOnSave": {
          "source.fixAll.ruff": "never",
          "source.organizeImports.ruff": "never"
        }
      }
    }
    ```

---

## ⚙️ 2. Customizing Without a `.toml` File

To ignore specific rules (like `print` statements or long lines) directly in VS Code:

1.  Go to **Settings** (`Ctrl+,`).
2.  Search for `Ruff Lint Args`.
3.  Click **Add Item** for each of these recommended arguments:

| Argument | Why? |
| :--- | :--- |
| `--ignore=T201` | **Allows `print()`** (Essential for your debug workflow). |
| `--ignore=E501` | Stops "Line too long" warnings. |
| `--select=E,F,I` | Enables **E**rrors, **F**lakes, and **I**sort (Import sorting). |

---

## 💡 3. Your New Workflow

Since we disabled "On Save" actions, use these three methods to manage your code quality:

### A. The "Visual" Way (Targeted)
* **The Squiggle:** Hover over any red/yellow line to see the error.
* **The Lightbulb 💡:** Click the bulb or press `Ctrl + .` to auto-fix that specific line.

### B. The "On-Demand" Way (Bulk)
* **Format Document:** Right-click anywhere and select **Format Document** (`Alt+Shift+F`) to clean up spacing.
* **Ruff Fix All:** Open Command Palette (`Ctrl+Shift+P`) and type `Ruff: Fix all auto-fixable problems`.

### C. The "To-Do List" Way (Overview)
* Press `Ctrl+Shift+M` to open the **Problems Tab**. This lists every issue in your file. Use it as a checklist before finishing your task.

---

## 🔍 4. Key Rule Reference

| Code | Name | Action |
| :--- | :--- | :--- |
| **F401** | Unused Import | Fix via Lightbulb or `Ruff: Fix all`. |
| **F821** | Undefined Name | **Fix immediately** (This is a bug/crash). |
| **T201** | Print Found | Ignored by our settings (for your debugging). |
| **I001** | Import Sorting | Keeps your `import` block clean and alphabetical. |

---

## 🧹 5. Moving to Production
When you are ready to swap `print()` for `logging`, simply:
1.  Remove `--ignore=T201` from your VS Code settings.
2.  All `print` statements will reappear in your **Problems Tab**.
3.  Address them one by one or delete them.