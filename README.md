# 🎭 Slow Print CLI — Interactive Python Program

This is a small Python program that creates an interactive experience using a slow typing effect in the terminal.  
It asks the user questions and responds with motivational messages animated using `slow_print()`.

---

## 🚀 Features

- ⌨️ User name and email input  
- 🧠 Reflective questions about life, freedom, and purpose  
- 🎬 Slow typing text effect (typewriter style)  
- 🧹 Automatic screen clearing after each response  
- 🔁 Interactive loop until the user chooses to exit  

---
## 📊 Program Flow Diagram (ASCII)

```
 ┌──────────────────────────┐
 │        Program Start     │
 └──────────────┬───────────┘
                │
                ▼
 ┌──────────────────────────┐
 │  Clear screen & greet    │
 │    (slow_print)          │
 └──────────────┬───────────┘
                │
                ▼
 ┌──────────────────────────┐
 │   Ask for user name      │
 └──────────────┬───────────┘
                │
                ▼
 ┌──────────────────────────┐
 │   Ask for user email     │
 └──────────────┬───────────┘
                │
                ▼
        ┌───────────────────┐
        │  Show main menu   │
        └───────┬───────────┘
                │
                ▼
      ┌───────────────────────┐
      │  User selects option  │
      └──────────┬────────────┘
                 │
     ┌───────────┼───────────────────────────────────────────┐
     │           │                       │                   │
     ▼           ▼                       ▼                   ▼
┌────────┐  ┌────────┐            ┌────────┐          ┌────────┐
│  Opt 1 │  │  Opt 2 │            │  Opt 3 │          │  Opt 4 │
└────┬───┘  └────┬───┘            └────┬───┘          └────┬───┘
     │           │                       │                   │
     ▼           ▼                       ▼                   ▼
 ┌────────────────────────────────────────────────────────────┐
 │ Display message using slow_print()                         │
 └────────────────────────────────────────────────────────────┘
                 │
                 ▼
      ┌───────────────────────┐
      │   Return to menu      │
      └──────────┬────────────┘
                 │
                 ▼
        ┌───────────────────┐
        │  User selects 0   │
        │      (Exit)       │
        └──────────┬────────┘
                   │
                   ▼
       ┌────────────────────────┐
       │  Show goodbye message  │
       └────────────────────────┘
```

---
## 📂 .gitignore

This project includes a `.gitignore` file to prevent unnecessary or auto-generated files from being tracked by Git.  
It ensures a clean repository and avoids committing Python cache folders and temporary files.

The `.gitignore` file ignores:
- `__pycache__/`
- Python bytecode files (`*.pyc`)
- Temporary system files
- Virtual environment folders (such as `venv/`)


## ▶️ How to Run

Make sure you have **Python 3** installed.

### 1️⃣ Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/slow-print-project.git

2️⃣ Enter the directory:
cd slow-print-project

3️⃣ Enter the directory:
cd slow-print-project

📝 License

This project is licensed under the MIT License.  
See the **LICENSE** file for more details.

⭐ Give the Repository a Star!

If this project helped you, leave a ⭐ on GitHub! It helps a lot.
