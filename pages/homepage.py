import tkinter as tk
import customtkinter

from Schema import models
from config import settings
from pages import admin_dashboard,product_list,cart

def homepage():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("400x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title("Shoppping Experince - Homepage")
    customtkinter.set_appearance_mode("System")

    user = models.Users.objects(username=settings.username).first()

    category_listbox = tk.Listbox(root_tk,yscrollcommand=True)
    category_listbox.pack(pady=10)
    categories = models.Category.objects()
    for category in categories:
        category_listbox.insert(tk.END, category.name)

    def select_category():
        selected_index = category_listbox.curselection()
        if not selected_index:
            tk.messagebox.showerror("Error", "Please select a category")
            return
        settings.category = category_listbox.get(selected_index)
        product_list.product_list()
        root_tk.destroy()

    select_category = customtkinter.CTkButton(root_tk, text="Select Category", command=select_category)
    select_category.pack(pady=10)

    if user.isAdmin:
        def admin_dashboard_btn_event():
            admin_dashboard.admin_dashboard()
            root_tk.destroy()
        admin_dashboard_btn = customtkinter.CTkButton(root_tk, text="Admin Dashboard", command=admin_dashboard_btn_event)
        admin_dashboard_btn.pack(pady=10)

    if user.cart != []:
        def cart_btn_event():
            cart.cart()
            root_tk.destroy()
        cart_btn = customtkinter.CTkButton(root_tk, text="View Cart", command=cart_btn_event)
        cart_btn.pack(pady=10)

    def logout_btn_event():
        tk.messagebox.showinfo("Success", "Feature Coming Soon")
        
    logout_btn = customtkinter.CTkButton(root_tk,text="Log Out", fg_color="red", hover_color="FireBrick", command=logout_btn_event)
    logout_btn.pack(pady=10)