import streamlit as st
import cx_Oracle

# Connect to the Oracle database
connection = cx_Oracle.connect('jack/swayam@localhost/XE')
cur = connection.cursor()

# Create a cursor object
cursor = connection.cursor()

def add_employee(employee_id, name, position, department, contact_number, salary, working_hours):
    cursor.execute("INSERT INTO Employee(EmployeeID, Name, Position, Department, ContactNumber, Salary, WorkingHours) "
                   "VALUES (:employee_id, :name, :position, :department, :contact_number, :salary, :working_hours)",
                   {"employee_id": employee_id, "name": name, "position": position, "department": department,
                    "contact_number": contact_number, "salary": salary, "working_hours": working_hours})
    connection.commit()

def search_employee(employee_id):
    cursor.execute("SELECT * FROM Employee WHERE EmployeeID = :employee_id", {"employee_id": employee_id})
    result = cursor.fetchall()
    return result

def delete_employee(employee_id):
    cursor.execute("DELETE FROM Employee WHERE EmployeeID = :employee_id", {"employee_id": employee_id})
    connection.commit()

# Streamlit app
st.set_page_config(page_title="Employee Management System", layout="wide")

# Header
st.title("Employee Management System")
st.write("---")

# Add employee
st.header("Add Employee")
col1, col2, col3 = st.columns(3)
with col1:
    employee_id = st.number_input("Employee ID", step=1)
with col2:
    name = st.text_input("Name")
with col3:
    position = st.text_input("Position")
col4, col5, col6 = st.columns(3)
with col4:
    department = st.text_input("Department")
with col5:
    contact_number = st.text_input("Contact Number")
with col6:
    salary = st.number_input("Salary", step=1)
working_hours = st.number_input("Working Hours", step=1)
if st.button("Add"):
    add_employee(employee_id, name, position, department, contact_number, salary, working_hours)
    st.success("Employee added successfully.")
st.write("---")

# Search employee
st.header("Search Employee")
search_employee_id = st.number_input("Enter Employee ID to search", step=1)
if st.button("Search"):
    result = search_employee(search_employee_id)
    if result:
        st.table(result)
    else:
        st.warning("No employee found.")
st.write("---")

# Delete employee
st.header("Delete Employee")
delete_employee_id = st.number_input("Enter Employee ID to delete", step=1)
if st.button("Delete"):
    delete_employee(delete_employee_id)
    st.success("Employee deleted successfully.")
st.write("---")

# Display all employees
st.header("Employee Information")
cursor.execute("SELECT * FROM Employee")
result = cursor.fetchall()
if result:
    st.table(result)
else:
    st.info("No employee data available.")
st.write("---")