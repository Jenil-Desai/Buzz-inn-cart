# app.py
import tkinter as tk
import customtkinter
from mongoengine import connect

from Schema import models
from config import settings
from pages import homepage

def connect_db():
    connect(host="mongodb://127.0.0.1:27017/shoppingExperince")

def app():
    connect_db()
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("400x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title("Shoppping Experince")
    customtkinter.set_appearance_mode("System")

    label = customtkinter.CTkLabel(master=root_tk, text="Welcome To Shoppping Experince", width=120, height=25, corner_radius=8)
    label.place(relx=0.2, rely=0.1)

    tab_view = customtkinter.CTkTabview(root_tk)
    tab_view.add("Login")
    tab_view.add("Sign Up")
    tab_view.place(relx=0.1,rely=0.2)

    username_entry = customtkinter.CTkEntry(tab_view.tab("Login"), placeholder_text="Enter Userename")
    username_entry.pack(padx=20, pady=10)

    password_entry = customtkinter.CTkEntry(tab_view.tab("Login"), placeholder_text="Enter Password")
    password_entry.pack(padx=20, pady=10)

    def login_btn_event():
        username = username_entry.get()
        if not username:
            tk.messagebox.showerror("Error", "Please enter a username")
            return
        password = password_entry.get()
        if not password:
            tk.messagebox.showerror("Error", "Please enter a password")
            return
        user = models.Users.objects(username=username,password=password).first()
        if user:
            settings.username = user.username
            homepage.homepage()
            root_tk.destroy()
        if not user:
            tk.messagebox.showerror("Error", "Please enter valid username or password")
            return

    login_btn = customtkinter.CTkButton(tab_view.tab("Login"), text="Login", command=login_btn_event)
    login_btn.pack(padx=20,pady=10)

    username_entry_signup = customtkinter.CTkEntry(tab_view.tab("Sign Up"), placeholder_text="Create Username")
    username_entry_signup.pack(padx=20,pady=10)

    password_entry_signup = customtkinter.CTkEntry(tab_view.tab("Sign Up"), placeholder_text="Create Password")
    password_entry_signup.pack(padx=20, pady=10)

    def signup_btn_event():
        username = username_entry_signup.get()
        if not username:
            tk.messagebox.showerror("Error", "Please enter a username")
            return
        password = password_entry_signup.get()
        if not password:
            tk.messagebox.showerror("Error", "Please enter a password")
            return
        new_user = models.Users(username=username,password=password)
        res = new_user.save()
        print(res)
        if res:
            tk.messagebox.showinfo("Success", "New Account Created Succesfully")
            settings.username = username
            homepage.homepage()
            root_tk.destroy()
        else:
            tk.messagebox.showerror("Error", "Enter Valid Username or Password")

    signup_btn = customtkinter.CTkButton(tab_view.tab("Sign Up"), text="Create Account" ,command=signup_btn_event)
    signup_btn.pack(padx=20,pady=10)

    root_tk.mainloop()

app()