import customtkinter

class LoginApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Login App")
        self.geometry("300x150")

        # Создаем поле для ввода логина
        self.username_entry = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.username_entry.pack(padx=20, pady=10)

        # Создаем поле для ввода пароля
        self.password_entry = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(padx=20, pady=10)

        # Создаем кнопку войти
        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(padx=20, pady=10)

    def login(self):
        # Здесь должна быть ваша логика входа в систему
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Закрываем окно входа и открываем основное окно
        self.withdraw()
        self.main_window = MainApp()

class MainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Main App")
        self.geometry("600x400")

        # Добавляем ваш функционал в основное окно
        self.label = customtkinter.CTkLabel(self, text="Welcome to the Main App!")
        self.label.pack(padx=20, pady=20)

        # Добавляем остальные элементы интерфейса
        # ...

        self.mainloop()

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()