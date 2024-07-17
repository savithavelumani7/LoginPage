# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 11:13:28 2024

@author: ELCOT
"""

import streamlit as st
import mysql.connector as sql
title=st.title("LoginPage")
st.header("Registration")

mydb=sql.connect(host="localhost",user="root",password="Savitha20")

def create_table():
    
    mycursor=mydb.cursor()
    mycursor.execute("Create Database if not exists LoginData")
    mycursor.execute("Use LoginData")
    mycursor.execute("""Create Table if not exists UserTable(
        id int auto_increment primary key,
        UserName varchar(50) not null,
        Password varchar(50) not null,
        age int,
        dob date,
        contact varchar(50)
                   )""")
    mycursor.close()
    




def insert_user(username_val,password_val):
    mycursor=mydb.cursor()
    mycursor.execute("Use LoginData")
    query="Insert into UserTable(UserName,Password) values (%s,%s)"
    mycursor.execute(query,(username_val,password_val))
    mydb.commit()
    mycursor.close()
    name=mycursor.fetchone()
    return name
    return 


def login(username_val,password_val):
    mycursor=mydb.cursor()

    mycursor.execute("Use LoginData")
    query="Select * from UserTable where username=%s and password=%s"
    mycursor.execute(query,(username_val,password_val))

def update(user_id,age,dob,contact):
    mycursor=mydb.cursor()
    mycursor.execute("Use LoginData")
    query="Update UserTable set age=%s,dob=%s,contact=%s where id=%s"
    mycursor.execute(query,(age,dob,contact,user_id))
    mydb.commit()
    mycursor.close()



def main():
    menu=["Login","Signup"]
    choice=st.sidebar.selectbox("Menu",menu)
    if choice=="Login":
        username_val=st.text_input("Enter Username:")
        password_val=st.text_input("Enter Password:",type="password")
        if st.button("Login"):
            user=insert_user(username_val,password_val)
            if user:
                
                st.success("Logged in Successfully")
                st.session_state.logged_in=True
                st.session_state.user=user
            else:
                st.warning("Incorrect username or password")
        if choice=="Signup":
            newuser=st.text_input("Create UserName:")
            newpassword=st.text_input("Create Password:",type="password")
            reenter=st.text_input("Reenter Password:",type="password")
            if st.button("SignUp"):
                if(newpassword==reenter):
                    if newuser and newpassword:
                        insert_user(newuser, newpassword)
                        st.success("Successfully Created")
                    else:
                        st.warning("Insufficient data")
                else:
                    st.warning("Passwords doesn't match")
        if "logged_in" in st.session_state and st.session_state.logged_in:
            user=st.session_state.user
            age=st.number_input("Age",value=user['age'] if user['age'] else 0)
            dob=st.date_input("Date Of Birth",value=user['dob'] if user['dob'] else None)
            contact=st.date_input("Contact",value=user['contact'] if user['contact'] else "None")
            if st.button("Update Profile"):
                update(user['id'],age,dob,contact)
                st.success("Profile Updated successfully")


if __name__=="__main__":
    main()

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            