import tkinter as tk
import customtkinter

from Schema import models
from config import settings
from pages import homepage

def product_list():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("400x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title(f"Shopping Experience - {settings.category}")
    customtkinter.set_appearance_mode("System")

    product_listbox = tk.Listbox(root_tk,width=35)
    product_listbox.pack(pady=10)
    category = models.Category.objects(name=settings.category).first()
    for product in category.products:
        product_listbox.insert(tk.END, f"{product.name} - {product.price}")
    
    def add_to_cart_event():
        selected_index = product_listbox.curselection()
        if not selected_index:
            tk.messagebox.showerror("Error", "Please select a product")
            return
        selected_product = product_listbox.get(selected_index)
        final_selected_product = selected_product.split('-')[0].strip()

        product = models.Products.objects(name=final_selected_product).first()
        models.Users.objects(username=settings.username).update_one(push__cart=product.id)
        tk.messagebox.showinfo("Success", "Product Added Successfully To Cart")

    add_to_cart = customtkinter.CTkButton(root_tk, text="Add To Cart", command=add_to_cart_event)
    add_to_cart.pack(pady=10)

    def back_to_homepage_event():
        homepage.homepage()
        root_tk.destroy()

    back_to_homepage = customtkinter.CTkButton(root_tk, text="Back To Homepage", command=back_to_homepage_event)
    back_to_homepage.pack(pady=10)