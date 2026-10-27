import customtkinter as ctk
from PIL import Image
import os


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_propagate(False)
        self.configure(width=kw.get("width", 400), height=kw.get("height", 400), fg_color="transparent")

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
        self.title_bank.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 5), sticky="")

        self.logo_label = ctk.CTkLabel(self, text="", image=self.logo_image)
        self.logo_label.grid(row=1, column=0, columnspan=2, pady=(5, 5), sticky="")

        self.username_label = ctk.CTkLabel(
            self,
            text="Username",
            font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
            text_color="#092453",
        )
        self.username_label.grid(row=2, column=0, padx=20, pady=(15, 5), sticky="w")

        self.user_entry = ctk.CTkEntry(
            self,
            placeholder_text="Username",
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
        self.user_entry.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(5, 5), sticky="")

        self.password_label = ctk.CTkLabel(self, text="Password",
                                           font=ctk.CTkFont(family="Arial", size=20, weight="bold"),
                                           text_color="#092453")
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
        self.password_entry.grid(row=5, column=0, columnspan=2, padx=(20, 20), pady=(5, 5), sticky="")

        self.login_btn = ctk.CTkButton(self, text="Login", width=200, height=50, border_width=3, corner_radius=10,
                                       font=ctk.CTkFont(family="Arial", size=20, weight="bold"), fg_color="#092453",
                                       command=lambda: self._on_click_login())
        self.login_btn.grid(row=6, column=0, columnspan=2, pady=(20, 5), sticky="")

    def _on_click_login(self):
        username: str = self.user_entry.get()
        password: str = self.password_entry.get()
        if username == "" or password == "":
            self.show_custom_warning("Missing Fields", "Please fill in all fields!")

    def show_custom_warning(self, title, message):
        popup = ctk.CTkToplevel(self)
        popup.geometry("320x160")
        popup.title(title)
        popup.resizable(False, False)
        popup.grab_set()

        msg_label = ctk.CTkLabel(
            popup,
            text=message,
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            text_color="#092453",
            wraplength=280,
        )
        msg_label.pack(pady=(25, 15))

        ok_btn = ctk.CTkButton(
            popup,
            text="OK",
            width=100,
            height=35,
            fg_color="#092453",
            text_color="#FFFFFF",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            command=popup.destroy,
        )
        ok_btn.pack(pady=10)


class SwitchPage(ctk.CTkFrame):
    def __init__(self, master, active_page, on_switch, **kw):
        super().__init__(master, **kw)
        self.grid_propagate(False)
        self.configure(width=kw.get("width", 400), height=kw.get("height", 120), fg_color="transparent")
        self.grid_columnconfigure(0, weight=1)

        self.active_page = active_page
        self.on_switch = on_switch

        # Determine button themes based on which page is currently active
        login_fg = "#092453" if self.active_page == "login" else "#E5E7EB"
        login_text = "#FFFFFF" if self.active_page == "login" else "#020618"

        signup_fg = "#092453" if self.active_page == "signup" else "#E5E7EB"
        signup_text = "#FFFFFF" if self.active_page == "signup" else "#020618"

        self.login_page_btn = ctk.CTkButton(
            self, text="Login", width=400, height=45, border_width=3, corner_radius=10,
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
            fg_color=login_fg, text_color=login_text,
            command=lambda: self.on_switch("login")
        )
        self.login_page_btn.grid(row=0, column=0, padx=40, pady=(5, 5), sticky="")

        self.signup_page_btn = ctk.CTkButton(
            self, text="Signup Page", width=400, height=45, border_width=3, corner_radius=10,
            font=ctk.CTkFont(family="Arial", size=18, weight="bold"),
            fg_color=signup_fg, text_color=signup_text,
            command=lambda: self.on_switch("signup")
        )
        self.signup_page_btn.grid(row=1, column=0, padx=40, pady=(5, 5), sticky="")

        self.setup_hover_effects()

    def setup_hover_effects(self):
        # Only add hover animation to the inactive/alternative page button
        if self.active_page == "login":
            self.login_page_btn.configure(hover=False)
            self.signup_page_btn.configure(hover=True)
            self.signup_page_btn.bind("<Enter>", lambda e: self.signup_page_btn.configure(text_color="#FFFFFF",
                                                                                          fg_color="#1C398E"))
            self.signup_page_btn.bind("<Leave>", lambda e: self.signup_page_btn.configure(text_color="#020618",
                                                                                          fg_color="#E5E7EB"))
        else:
            self.signup_page_btn.configure(hover=False)
            self.login_page_btn.configure(hover=True)
            self.login_page_btn.bind("<Enter>",
                                     lambda e: self.login_page_btn.configure(text_color="#FFFFFF", fg_color="#1C398E"))
            self.login_page_btn.bind("<Leave>",
                                     lambda e: self.login_page_btn.configure(text_color="#020618", fg_color="#E5E7EB"))


class SignupPage(ctk.CTkFrame):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)
        self.grid_propagate(False)
        self.configure(width=kw.get("width", 400), height=kw.get("height", 400), fg_color="transparent")

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
        self.title_bank.grid(row=0, column=0, columnspan=2, padx=10, pady=(20, 5), sticky="")

        self.logo_label = ctk.CTkLabel(self, text="", image=self.logo_image)
        self.logo_label.grid(row=1, column=0, columnspan=2, pady=(5, 5), sticky="")

        self.username_entry = ctk.CTkEntry(
            self,
            placeholder_text="Username",
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
        self.username_entry.grid(row=2, column=0, columnspan=2, pady=(15, 5), sticky="")

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
        self.password_entry.grid(row=3, column=0, columnspan=2, pady=(5, 5), sticky="")

        self.com_password_entry = ctk.CTkEntry(
            self,
            placeholder_text="Confirm password",
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
        self.com_password_entry.grid(row=4, column=0, columnspan=2, pady=(5, 5), sticky="")

        self.register_btn = ctk.CTkButton(self, text="Register", width=200, height=50, border_width=3, corner_radius=10,
                                          font=ctk.CTkFont(family="Arial", size=20, weight="bold"), fg_color="#092453" , command=self.on_click_register)
        self.register_btn.grid(row=5, column=0, columnspan=2, pady=(15, 5), sticky="")

    def on_click_register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        com_password = self.com_password_entry.get()

        if username == "" or password == "" or com_password == "":
            self.show_custom_warning("Missing Fields", "Please fill in all fields!")

    def show_custom_warning(self, title, message):
        popup = ctk.CTkToplevel(self)
        popup.geometry("320x160")
        popup.title(title)
        popup.resizable(False, False)
        popup.grab_set()

        msg_label = ctk.CTkLabel(
            popup,
            text=message,
            font=ctk.CTkFont(family="Arial", size=16, weight="bold"),
            text_color="#092453",
            wraplength=280,
        )
        msg_label.pack(pady=(25, 15))

        ok_btn = ctk.CTkButton(
            popup,
            text="OK",
            width=100,
            height=35,
            fg_color="#092453",
            text_color="#FFFFFF",
            font=ctk.CTkFont(family="Arial", size=12, weight="bold"),
            command=popup.destroy,
        )
        ok_btn.pack(pady=10)
