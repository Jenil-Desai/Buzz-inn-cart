import tkinter as tk
import customtkinter

from Schema import models
from config import settings
from pages import homepage,checkout

def cart():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("400x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title("Shoppping Experince - Cart")
    customtkinter.set_appearance_mode("System")

    cart_listbox = tk.Listbox(root_tk,yscrollcommand=True,width=35)
    cart_listbox.pack(pady=10)
    user = models.Users.objects(username=settings.username).first()
    for product in user.cart:
        cart_listbox.insert(tk.END, f"{product.name} - {product.price}")

    def checkout_btn_event():
        checkout.checkout()
        root_tk.destroy()

    checkout_btn = customtkinter.CTkButton(root_tk,text="Checkout Now", command=checkout_btn_event)
    checkout_btn.pack(pady=10)

    def clear_cart_btn_event():
        models.Users.objects(username=settings.username).update_one(cart=[])
        tk.messagebox.askquestion("askquestion", "Are you sure?")
        tk.messagebox.showinfo("Success", "Cart Cleared Successfully")
        homepage.homepage()
        root_tk.destroy()
    
    clear_cart_btn = customtkinter.CTkButton(root_tk, text="Clear Cart", command=clear_cart_btn_event)
    clear_cart_btn.pack(pady=10)

    def back_to_homepage_event():
        homepage.homepage()
        root_tk.destroy()

    back_to_homepage = customtkinter.CTkButton(root_tk, text="Back To Homepage", command=back_to_homepage_event)
    back_to_homepage.pack(pady=10)