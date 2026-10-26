import logging

import customtkinter as ctk
from PIL import Image
import os

class Frame(ctk.CTkFrame):

    def __init__(self, master, **kw):
      super().__init__(master, **kw)
      self.grid_propagate(False)
      self.configure(width=kw.get("width", 400), height=kw.get("height", 400))

      # ADD THIS LINE: Tells column 0 to expand and center its contents horizontally
      self.grid_columnconfigure(0, weight=1)

      self.logo_file = Image.open(os.path.join(".", "images", "Logo.png"))
      self.logo_image = ctk.CTkImage(
          light_image=self.logo_file, dark_image=self.logo_file, size=(160, 120)
      )

      self.title_bank = ctk.CTkLabel(
          self,
          text="BANKING SYSTEM",
          font=ctk.CTkFont(family="Arial", size=40, weight="bold"),
          text_color="#092453",
      )
      self.title_bank.grid(
          row=0, column=0, columnspan=2, padx=10, pady=(20, 5), sticky=""
      )

      self.logo_label = ctk.CTkLabel(self, text="", image=self.logo_image)
      self.logo_label.grid(row=1, column=0, columnspan=2, pady=(5, 5), sticky="")

      self.username_label = ctk.CTkLabel(
          self,
          text="Username",
          font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
          text_color="#092453",
      )
      self.username_label.grid(
          row=2, column=0, padx=20, pady=(15, 5), sticky="w"
      )

      self.user_icon_file = Image.open(os.path.join("." , "images" , "user_icon.png"))
      self.user_icon = ctk.CTkImage(light_image=self.user_icon_file , dark_image=self.user_icon_file  , size=(40,40))

      self.user_icon_label = ctk.CTkLabel(self , text="" , image=self.user_icon)
      self.user_icon_label.grid(row=3 , column=0 ,padx=25 ,pady=(5,5),sticky="w")

      self.user_entry = ctk.CTkEntry(
         self ,
         placeholder_text="Username" ,
         width=450,
         height=50,
         corner_radius=10,
         fg_color="#ffffff",
         placeholder_text_color="#828385",
         border_color="#092453",
         border_width=3,
         text_color="#000000",
         font=ctk.CTkFont(family="Arial", size=15, weight="bold")
      )
      self.user_entry.grid(
         row=3 , column=0 ,columnspan=2 , padx=(70,30) , pady=(5,5) , sticky="w"
      )

      self.lock_icon_file = Image.open(os.path.join("." , "images" , "lock_icon.png"))
      self.lock_icon = ctk.CTkImage(light_image=self.lock_icon_file , dark_image=self.lock_icon_file , size=(48,48))

      self.lock_icon_label = ctk.CTkLabel(self , text="" , image=self.lock_icon)
      self.lock_icon_label.grid(row=5 , column=0 ,padx=25 ,pady=(5,5),sticky="w")


      self.password_label = ctk.CTkLabel(self, text="Password", font=ctk.CTkFont(family="Arial", size=20, weight="bold"), text_color="#092453", )
      self.password_label.grid(row=4, column=0, padx=20, pady=(5, 5), sticky="w")
      self.password_entry = ctk.CTkEntry(
         self,
         placeholder_text="Enter your password",
         width=450,
         height=50,
         corner_radius=10,
         fg_color="#ffffff",
         placeholder_text_color="#828385",
         border_color="#092453",
         border_width=3,
         text_color="#000000",
         font=ctk.CTkFont(family="Arial", size=15, weight="bold"),
         show="•"
         )
      self.password_entry.grid(row=5, column=0, columnspan=2, padx=(70, 30), pady=(5, 5), sticky="w")

      self.login_btn = ctk.CTkButton(self , text="Login" , width=200 , height=50 , border_width=3 , corner_radius=10 , font=ctk.CTkFont(family="Arial", size=20, weight="bold") ,fg_color="#092453" , command=lambda:self._on_click_login())
      self.login_btn.grid(row=6 , column=0 ,columnspan=2 , padx=(50,30) , pady=(10,5) , sticky="n")

    def _on_click_login(self):
        username:str = self.user_entry.get()
        password:str = self.password_entry.get()
        if username == "" or password == "":
            self.show_custom_warning("Missing Fields", "Please fill in all fields!")

    def show_custom_warning(self, title, message):
        # 1. Create a top-level pop-up window
        popup = ctk.CTkToplevel(self)
        popup.geometry("320x160")
        popup.title(title)
        popup.resizable(False, False)

        # Make the popup modal (locks focus to the popup until closed)
        popup.grab_set()

        # 2. Warning Message Label
        msg_label = ctk.CTkLabel(
            popup,
            text=message,
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color="#092453",
            wraplength=280,
        )
        msg_label.pack(pady=(25, 15))

        # 3. OK Button to close the warning
        ok_btn = ctk.CTkButton(
            popup,
            text="OK",
            width=100,
            height=35,
            fg_color="#092453",
            text_color="#FFFFFF",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            command=popup.destroy,  # Closes the pop-up window
        )
        ok_btn.pack(pady=10)

class SwitchPage(ctk.CTkFrame):
    def __init__(self , master , **kw):
        super().__init__(master, **kw)
        self.grid_propagate(False)
        self.configure(width=kw.get("width", 400), height=kw.get("height", 400))
        self.page_name = "login"

        self.login_page_btn = ctk.CTkButton(self , text="Login" , width=400, height=50 , border_width=3 , corner_radius=10 , font=ctk.CTkFont(family="Arial", size=20, weight="bold") ,fg_color="#092453" , text_color="#FFFFFF")
        self.login_page_btn.grid(row=0 , column=0 , padx=40 , pady=(10,5) , sticky="")

        self.signup_page_btn = ctk.CTkButton(self , text="Signup Page" , width=400, height=50 , border_width=3 , corner_radius=10 , font=ctk.CTkFont(family="Arial", size=20, weight="bold") ,fg_color="#E5E7EB" , text_color="#020618")
        self.signup_page_btn.grid(row=1 , column=0 , padx=40 , pady=(10,5) , sticky="")

        self.check_hover()

    def check_hover(self):
        if self.page_name == "login":
            # 2. Signup button hover behavior
            self.login_page_btn.configure(hover=False)
            self.signup_page_btn.configure(hover=True)
            self.signup_page_btn.bind(
                "<Enter>",
                lambda e: self.signup_page_btn.configure(
                    text_color="#FFFFFF", fg_color="#1C398E"
                ),
            )
            self.signup_page_btn.bind(
                "<Leave>",
                lambda e: self.signup_page_btn.configure(
                    text_color="#020618", fg_color="#FFFFFF"
                ),
            )
        else:
            self.login_page_btn.configure(hover=True)
            self.signup_page_btn.configure(hover=False)
            self.login_page_btn.bind(
                "<Enter>",
                lambda e: self.login_page_btn.configure(
                    text_color="#FFFFFF", fg_color="#1C398E"
                ),
            )
            self.login_page_btn.bind(
                "<Leave>",
                lambda e: self.login_page_btn.configure(
                    text_color="#020618", fg_color="#FFFFFF"
                ),
            )

    def on_enter(self , event):
        if self.page_name != "login":
            self.signup_page_btn.configure(text_color="#FFFFFF" , fg_color="#1C398E")
            return
        else:
            self.login_page_btn.configure(text_color="#FFFFFF", fg_color="#1C398E")
            return

    def on_leave(self , event):
        if self.page_name != "login":
            self.signup_page_btn.configure(text_color="#020618" , fg_color="#FFFFFF")
            return
        else:
            self.login_page_btn.configure(text_color="#020618", fg_color="#FFFFFF")
            return
class LoginFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.resizable(False, False)
        self.configure(fg_color="#E8EAEC")
        self.grid_columnconfigure(0 , weight=1)
        self.grid_rowconfigure(0 , weight=1)
        self.login_frame = Frame(master=self , width=480 , height=500)
        self.login_frame.grid(row=0 , column=0 , padx=10 , pady=0 ,sticky="")

        self.switch_page = SwitchPage(master=self , width=480 , height=150)
        self.switch_page.grid(row=1 , column=0 , padx=10 , pady=(0,20) ,sticky="")