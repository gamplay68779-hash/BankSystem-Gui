import customtkinter as ctk
from ui_login import LoginFrame, SwitchPage, SignupPage


class MainFrame(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x700")
        self.resizable(False, False)
        self.configure(fg_color="#E8EAEC")

        # Configure root grid weights to center the cards properly
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=4)  # For the form card
        self.grid_rowconfigure(1, weight=1)  # For the switch buttons card

        self.active_page_frame = None
        self.switch_frame = None

        # Start by showing the login view
        self.show_login()

    def show_login(self):
        # Destroy previous frames if they exist to prevent overlapping layers
        if self.active_page_frame:
            self.active_page_frame.destroy()
        if self.switch_frame:
            self.switch_frame.destroy()

        self.title("Login Page")

        # Create and place Login form
        self.active_page_frame = LoginFrame(master=self, width=480, height=500)
        self.active_page_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="n")

        # Create and place Switch navigation panel (passing "login" state and callback function)
        self.switch_frame = SwitchPage(master=self, active_page="login", on_switch=self.handle_page_switch, width=480,
                                       height=120)
        self.switch_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="n")

    def show_signup(self):
        # Destroy previous frames if they exist
        if self.active_page_frame:
            self.active_page_frame.destroy()
        if self.switch_frame:
            self.switch_frame.destroy()

        self.title("Signup Page")

        # Create and place Signup form
        self.active_page_frame = SignupPage(master=self, width=480, height=500)
        self.active_page_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="n")

        # Create and place Switch navigation panel (passing "signup" state and callback function)
        self.switch_frame = SwitchPage(master=self, active_page="signup", on_switch=self.handle_page_switch, width=480,
                                       height=120)
        self.switch_frame.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="n")

    def handle_page_switch(self, target_page: str):
        if target_page == "login":
            self.show_login()
        elif target_page == "signup":
            self.show_signup()


def main():
    app = MainFrame()
    app.mainloop()


if __name__ == "__main__":
    main()