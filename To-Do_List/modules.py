import sqlite3

conn = sqlite3.connect(database = "data_base.db" , check_same_thread = False)
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS tasks_table(task TEXT , task_status TEXT , task_due_date Date)")

def add_data(task , task_status , task_due_date):
    c.execute("INSERT INTO tasks_table(task , task_status , task_due_date) VALUES(? , ? , ?)" , (task , task_status , task_due_date))
    conn.commit()

def view_data():
    c.execute("SELECT * FROM tasks_table")
    data = c.fetchall()
    return data

def view_unique_task():
    c.execute("SELECT DISTINCT task FROM tasks_table")
    data = c.fetchall()
    return data

def get_task(task):
    c.execute(f"SELECT * FROM tasks_table WHERE task = '{task}'")
    data = c.fetchall()
    return data

def edit_task(new_task , new_task_status , new_task_due_date , task , task_status , task_due_date):
    c.execute(f"UPDATE tasks_table SET task = ? , task_status = ? , task_due_date = ? WHERE  task = ? and task_status = ? and task_due_date = ?" , (new_task , new_task_status , new_task_due_date , task , task_status , task_due_date))
    conn.commit()
    data = c.fetchall()
    return data

def delete_data(task):
    c.execute("DELETE FROM tasks_table WHERE task = '{}'".format(task))
    conn.commit()
