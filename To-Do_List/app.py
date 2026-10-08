import streamlit as st 
from modules import create_table , add_data , view_data , view_unique_task , get_task , edit_task , delete_data
import pandas as pd
import plotly.express as px

HTML_BANNER = """
<h1 style = "text-align : center; 
             color : #4f46E5;
             font-size : 48px;
             font-weight : 700;
             margin-bottom : 0;">✨ To-Do List</h1>

<p style = "text-align : center; color : #6B7280; font-size : 18px; margin-top : 5px;">Organize your tasks. Stay focused. Get things done.</p>
"""
HTML_CREATE = """
<h1 style = "text-align : center; 
             color : #4f46E5;
             font-size : 48px;
             font-weight : 700;
             margin-bottom : 0;">Add Items</h1>
"""
HTML_READ = """
<h1 style = "text-align : center; 
             color : #4f46E5;
             font-size : 48px;
             font-weight : 700;
             margin-bottom : 0;">View Items</h1>
"""
HTML_UPDATE = """
<h1 style = "text-align : center; 
             color : #4f46E5;
             font-size : 48px;
             font-weight : 700;
             margin-bottom : 0;">Update Items</h1>
"""
HTML_DELETE = """
<h1 style = "text-align : center; 
             color : #4f46E5;
             font-size : 48px;
             font-weight : 700;
             margin-bottom : 0;">Delete Items</h1>
"""
def main():
    choice = st.sidebar.selectbox(label = "Menu" , options = ["Home" , "Create" , "Read" , "Update" , "Delete"])
    create_table()

    if choice == "Home":
        st.markdown(body = HTML_BANNER , unsafe_allow_html = True)
        with st.expander(label = "To Do List" , expanded = True):
            st.info("Welcome to your To-Do App 📝")
            st.markdown("""A simple and intuitive task management app designed to help you organize your daily tasks and stay productive.
                        With this app, you can easily **Create**, **Read**, **Update**, **View**, and **Delete** your tasks. Whether you want to add a new task, check your existing tasks, update their details, or remove completed tasks, everything is managed in one place.
                        Stay organized, keep track of your tasks, and get things done! 🚀""")




    elif choice == "Create":
        st.markdown(body = HTML_CREATE , unsafe_allow_html = True)
        with st.expander(label = "Add Items" , expanded = True):    
            col1 , col2 = st.columns(spec = 2)
            with col1:
                task = st.text_area(label = "Task To Do")
            with col2:
                task_status = st.selectbox(label = "Status" , options = ["To Do" , "Doing" , "Done"])
                task_due_date = st.date_input(label = "Due Date")
            if st.button(label = "Add Task" , type = "primary"):
                add_data(task = task , task_status = task_status , task_due_date = task_due_date)
                st.success(f"Successfully Added Data : {task}")
    
    elif choice == "Read":
        st.markdown(body = HTML_READ , unsafe_allow_html = True)
        result = view_data()
        with st.expander(label = "View Data" , expanded = True):
            df = pd.DataFrame(data = result , columns = ["Task" , "Status" , "Date"])
            st.dataframe(df)
        with st.expander(label = "Task Status"):
            task_df = df["Status"].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            st.plotly_chart(px.pie(data_frame = task_df , names = "Status" , values = "count"))
    
    elif choice == "Update":
        st.markdown(HTML_UPDATE , unsafe_allow_html = True)
        result = view_data()
        df = pd.DataFrame(result , columns = ["Task" , "Status" , "Date"])
        with st.expander("Current Data"):
            st.dataframe(df)

        selected_task = st.selectbox(label = "Task To Edit" , options = [i[0] for i in view_unique_task()])
        selected_result = get_task(selected_task)
        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]
            col1 , col2 = st.columns(spec = 2)
            with col1:
                new_task = st.text_area("Task To Do", task)
            with col2:
                new_task_status = st.selectbox(task_status , ["ToDo" , "Doing" , "Done"])
                new_task_due_date = st.date_input(task_due_date)
            if st.button("Update Task"):
                edit_task(new_task , new_task_status , new_task_due_date , task , task_status , task_due_date)
                st.success("Successfully Updated:: {} To :: {}".format(task , new_task))
            with st.expander("View Updated Data"):
                result2 = view_data()
                df2 = pd.DataFrame(result2 , columns = ["Task" , "Status" , "Date"])
                st.dataframe(df2)

    elif choice == "Delete":
        st.markdown(body = HTML_DELETE , unsafe_allow_html = True)
        with st.expander(label = "View Data"):
            result = view_data()
            clean_df = pd.DataFrame(result , columns = ["Task" , "Status" , "Date"])
            st.dataframe(clean_df)
            delete_by_task_name = st.selectbox(label = "Select Task For Delete" , options = [i[0] for i in view_unique_task()])
            if st.button(label = "Delete"):
                delete_data(delete_by_task_name)
                st.success(f"Deleted : {delete_by_task_name}")
            with st.expander("Updated Data"):
                result = view_data()
                clean_df = pd.DataFrame(result , columns = ["Task" , "Status" , "Date"])
                st.dataframe(clean_df)

if __name__ == "__main__":
    main()