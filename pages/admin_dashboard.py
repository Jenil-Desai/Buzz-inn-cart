import tkinter as tk
import customtkinter

from Schema import models
from pages import homepage

def admin_dashboard():
    root_tk = tk.Tk()  # create the Tk window like you normally do
    root_tk.geometry("450x350")
    root_tk.resizable(width=False,height=False)
    root_tk.title("Shoppping Experince - Admin Dashboard")
    customtkinter.set_appearance_mode("System")


    tab_view = customtkinter.CTkTabview(root_tk)
    tab_view.add("Add Category")
    tab_view.add("Add Product")
    tab_view.add("Delete Category")
    tab_view.add("Delete Product")
    tab_view.pack(pady=10)

    category_name_entry = customtkinter.CTkEntry(tab_view.tab("Add Category"), placeholder_text="Enter Category Name")
    category_name_entry.pack(padx=20, pady=10)

    def add_category_btn_event():
        category = category_name_entry.get()
        if not category:
            tk.messagebox.showerror("Error", "Please enter category name")
            return
        new_category = models.Category(name=category)
        new_category.save()
        tk.messagebox.showinfo("Success", "New Category Successfully")

    add_category_btn = customtkinter.CTkButton(tab_view.tab("Add Category"), text="Add Category", command=add_category_btn_event)
    add_category_btn.pack(pady=5)

    product_name_entry = customtkinter.CTkEntry(tab_view.tab("Add Product"), placeholder_text="Enter Product Name")
    product_name_entry.pack(padx=20,pady=10)

    product_price_entry = customtkinter.CTkEntry(tab_view.tab("Add Product"), placeholder_text="Enter Product Price")
    product_price_entry.pack(padx=20,pady=10)

    categories = [category.name for category in models.Category.objects()]
    product_category_optionMenu = customtkinter.CTkOptionMenu(tab_view.tab("Add Product"), values=categories)
    product_category_optionMenu.set(categories[0])
    product_category_optionMenu.pack(pady=10)

    def add_product_btn_event():
        product_category = product_category_optionMenu.get()
        product_name = product_name_entry.get()
        if not product_name:
            tk.messagebox.showerror("Error", "Please enter product name")
            return
        product_price = product_price_entry.get()
        if not product_price:
            tk.messagebox.showerror("Error", "Please enter product price")
            return
        new_product = models.Products(name=product_name,price=product_price)
        new_product.save()
        models.Category.objects(name=product_category).update_one(push__products=new_product.id)
        tk.messagebox.showinfo("Success", "New Product Added Succesfully")

    add_product_btn = customtkinter.CTkButton(tab_view.tab("Add Product"), text="Add Product", command=add_product_btn_event)
    add_product_btn.pack(pady=10)


    def back_to_homepage_event():
        homepage.homepage()
        root_tk.destroy()

    back_to_homepage = customtkinter.CTkButton(root_tk, text="Back To Homepage", command=back_to_homepage_event)
    back_to_homepage.pack(pady=10)