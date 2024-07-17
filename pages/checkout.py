import tkinter as tk
import customtkinter

from Schema import models
from config import settings
from pages import homepage

def checkout():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("400x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title("Shoppping Experince - Checkout")
    customtkinter.set_appearance_mode("System")

    cart_listbox = tk.Listbox(root_tk,yscrollcommand=True,width=35)
    cart_listbox.pack(pady=10)
    user = models.Users.objects(username=settings.username).first()
    total = 0
    for product in user.cart:
        cart_listbox.insert(tk.END, f"{product.name} - {product.price}")
        total = total + product.price

    total_value = customtkinter.CTkLabel(root_tk,text=f"Total Amount = {total}",justify="center",)
    total_value.pack(pady=10)

    def order_now_btn_event():
        tk.messagebox.askquestion("askquestion", "Are you sure?")
        models.Users.objects(username=settings.username).update_one(cart=[])
        tk.messagebox.showinfo("Success", "Thanks For Buying - Visti Again")
        homepage.homepage()
        root_tk.destroy()
    
    order_now_btn = customtkinter.CTkButton(root_tk,text="Order Now", command=order_now_btn_event)
    order_now_btn.pack(pady=10)

    def back_to_homepage_event():
        homepage.homepage()
        root_tk.destroy()

    back_to_homepage = customtkinter.CTkButton(root_tk, text="Back To Homepage", command=back_to_homepage_event)
    back_to_homepage.pack(pady=10)