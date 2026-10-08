# ✨ To-Do List App

A simple and intuitive task management web app built with **Streamlit** and **SQLite**. Organize your daily tasks, track their progress, and visualize your workload — all in one clean interface.

> Organize your tasks. Stay focused. Get things done.

---

## 📌 Features

- **Create** tasks with a description, a status, and a due date
- **Read** all tasks in an interactive table
- **Update** any existing task (text, status, and due date)
- **Delete** tasks you no longer need
- **Status overview** with a summary table and an interactive **pie chart** (Plotly)
- **Persistent storage** using a local SQLite database — your tasks are saved between sessions
- Clean, centered UI with a sidebar menu for easy navigation

### Task Statuses

| Status  | Meaning                  |
|---------|--------------------------|
| To Do   | Not started yet          |
| Doing   | Currently in progress    |
| Done    | Completed                |

---

## 🛠️ Tech Stack

| Tool        | Purpose                                  |
|-------------|------------------------------------------|
| Python 3.8+ | Core language                            |
| Streamlit   | Web interface                            |
| SQLite3     | Lightweight local database (built into Python) |
| Pandas      | Data handling and tabular display        |
| Plotly      | Interactive charts                       |

---

## 📁 Project Structure

```
.
├── app.py          # Streamlit UI: pages, forms, tables, and charts
├── modules.py      # Database layer: connection and CRUD functions
├── data_base.db    # SQLite database (auto-created on first run)
└── README.md
```

### How the code is organized

- **`app.py`** renders the interface. A sidebar menu switches between five pages: *Home, Create, Read, Update,* and *Delete*.
- **`modules.py`** handles everything related to the database:

| Function              | Description                                  |
|-----------------------|----------------------------------------------|
| `create_table()`      | Creates the `tasks_table` if it doesn't exist |
| `add_data()`          | Inserts a new task                           |
| `view_data()`         | Returns all tasks                            |
| `view_unique_task()`  | Returns distinct task names                  |
| `get_task()`          | Fetches a task by its name                   |
| `edit_task()`         | Updates a task's text, status, and due date  |
| `delete_data()`       | Deletes a task by its name                   |

### Database Schema

```sql
CREATE TABLE IF NOT EXISTS tasks_table(
    task TEXT,
    task_status TEXT,
    task_due_date Date
);
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install streamlit pandas plotly
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 🧭 Usage

1. **Home** – A short overview of the app.
2. **Create** – Write your task, choose a status and a due date, then click **Add Task**.
3. **Read** – Browse all your tasks in a table and check the **Task Status** section for a pie chart of your progress.
4. **Update** – Pick a task from the dropdown, edit its details, and click **Update Task**.
5. **Delete** – Select a task and click **Delete** to remove it.

---

## 🔮 Future Improvements

- Add a unique ID for each task to safely handle duplicate task names
- Use fully parameterized SQL queries everywhere
- Add search, filtering, and sorting
- Highlight overdue tasks
- User authentication and multi-user support

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
