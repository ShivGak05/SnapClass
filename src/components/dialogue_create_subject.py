import streamlit as st
from src.database.db import create_subject

@st.dialog("Create New Subject")
def dialogue_create_subject(teacher_id):
    st.write("Enter the details of new subject")
    sub_id=st.text_input("subject_code",placeholder="CS1001")
    sub_name=st.text_input("Subject Name",placeholder="Introduction to Computer Science")
    sub_section=st.text_input("Section",placeholder="A")

    if st.button("Create Subject Now",type='primary',width='stretch'):
        if sub_id and sub_name and sub_section:
            try:
                create_subject(sub_id,sub_name,sub_section,teacher_id)
                st.toast("Subject created successfully!")
                st.rerun()
            except Exception as e:
                st.error("Error")
        else:
            st.warning("Please fill all the details!")