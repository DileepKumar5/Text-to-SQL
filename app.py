from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##provide sql query
def get_gemini_reponse(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


#retrive
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()

    for row in rows:
        print(row)
        return rows
    

prompt=[
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has a table named EMPLOYEE with the following columns - NAME, LOCATION, POSITION, SALARY.
    For example:
    Example 1 - How many employees are in the database?, the SQL command will be something like:
    SELECT COUNT(*) FROM EMPLOYEE;
    Example 2 - Show all employees who work as 'Software Engineer', the SQL command will be something like:
    SELECT * FROM EMPLOYEE WHERE POSITION = 'Software Engineer';
    Example 3 - What is the average salary of employees in 'Berlin, Germany'?, the SQL command will be something like:
    SELECT AVG(SALARY) FROM EMPLOYEE WHERE LOCATION = 'Berlin, Germany';
    Please generate the SQL code without using ``` at the beginning or end of the code. All SQL keywords should be in capital letters.
    """
    ]


st.set_page_config(page_title="I can Retrive any SQL query")
st.header("Text to SQL Query")

question=st.text_input("Input: ",key=input)

submit=st.button("Ask the question")

if submit:
    response=get_gemini_reponse(question,prompt)
    st.subheader("Generated SQL Query:")
    st.code(response, language='sql')
    print(response)
    data = read_sql_query(response, "employee.db")
    st.subheader("The Reponse is ")
    for row in data:
        print(row)
        st.header(row)
