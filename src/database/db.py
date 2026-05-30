from src.database.config import supabase
import bcrypt

def check_user_exists(username):
    #checks if teacher already exists in database
    response=supabase.table("teachers").select("username").eq("username",username).execute()
    return len(response.data)>0

def hash_pass(pwd):
    return bcrypt.hashpw(pwd.encode(), bcrypt.gensalt()).decode()

def create_teacher(username,password,name):
    data={
        "username":username,
        "password":hash_pass(password),
        "name":name
    }
    response=supabase.table("teachers").insert(data).execute()
    return response.data

def check_pass(pwd,hashed):
    return bcrypt.checkpw(pwd.encode(), hashed.encode())

def teacher_login(username,password):
    response=supabase.table("teachers").select("*").eq("username",username).execute()
    if response.data:
        teacher=response.data[0]
        if check_pass(password,teacher['password']):
            return teacher
    return None

def get_all_students():
    response=supabase.table("students").select("*").execute()
    return response.data