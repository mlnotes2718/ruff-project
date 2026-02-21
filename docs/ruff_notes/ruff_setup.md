Here is your final, consolidated guide. You can copy this entire block and save it as `RUFF_SETUP.md` in your project folder for easy reference.

---

# 🚀 Ruff VS Code Setup (No-TOML Edition)

This configuration is designed for a **clean, distraction-free** workflow. It allows for `print()` statements during debugging, enforces the **88-character** modern standard, and works perfectly with **Auto Save** enabled.

---

## 🛠️ 1. The Configuration

Paste this into your `settings.json` (`Ctrl+Shift+P` > **Open User Settings (JSON)**).

```json
{
    "workbench.colorTheme": "Default Light Modern",
    
    // Auto Save: Work safely without manual saving
    "files.autoSave": "afterDelay",
    "files.autoSaveDelay": 1000,

    // Python Integration: Ruff as the primary tool
    "[python]": {
        "editor.defaultFormatter": "charliermarsh.ruff",
        "editor.formatOnSave": false, // Prevents code jumping while typing
        "editor.codeActionsOnSave": {
            "source.fixAll.ruff": "never",
            "source.organizeImports.ruff": "never"
        }
    },

    // Ruff Modern Settings
    "ruff.lineLength": 88,
    "ruff.lint.select": ["E", "F", "I"],
    "ruff.lint.ignore": ["T201"], // Allows print() statements
    
    // Visual Aids
    "editor.rulers": [88],
    "editor.renderWhitespace": "selection" 
}

```

---

## 💡 2. Daily Workflow

### **During Development**

* **Prints:** Use `print("debug")` as much as you want. Ruff will not flag them as errors.
* **The Ruler:** Watch the vertical line at **88 characters**. If your code crosses it, Ruff will suggest a fix (Rule E501).
* **Real-time Errors:** If you see a **Red Squiggle**, it’s a logic error (like a typo). Fix these immediately.

### **Cleaning Up**

Since "Format on Save" is off, you control when the code gets tidied:

1. **Right-Click > Format Document**: This fixes indentation, adds spaces around operators (`x=1` → `x = 1`), and wraps long lines.
2. **Organize Imports**: Use the Command Palette (`Ctrl+Shift+P`) and type "Ruff: Organize Imports" to sort your `import` statements alphabetically.

---

## 🔍 3. Common Rule Reference

| Code | Meaning | Behavior |
| --- | --- | --- |
| **T201** | `print` found | **Ignored** (Safe for debugging) |
| **E501** | Line too long | **Active** (Shows squiggle at 88 chars) |
| **F401** | Unused Import | **Active** (Helps keep code clean) |
| **F821** | Undefined Name | **Active** (Catches crashes/typos) |

---

## 🏁 4. Moving to Production

When you are ready to finalize your code and replace `print()` with proper logging:

1. Temporarily change `"ruff.lint.ignore": ["T201"]` to `"ruff.lint.ignore": []`.
2. Open the **Problems Tab** (`Ctrl+Shift+M`).
3. Every `print` statement in your project will now be listed as a task for you to complete.

**You're all set! Is there any other part of your Python workflow you'd like to optimize?**