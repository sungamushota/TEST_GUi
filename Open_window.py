import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("CustomTkinter example_background_image.py")
        self.geometry(f"{self.width}x{self.height}")
       # self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/test_images/bg_gradient.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create login frame
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="CustomTkinter\nLogin Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(100, 15))
        self.username_entry = customtkinter.CTkEntry(self.login_frame, width=200, placeholder_text="username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.password_entry = customtkinter.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Login", command=self.login_event, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.decription_button = customtkinter.CTkButton(self.login_frame, text="Description", command=self.description_event, width=200)
        self.decription_button.grid(row=4, column=0, padx=30, pady=(15, 15))

        #Create Test description Frame
        self.Description_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.Description_frame.grid_columnconfigure(0, weight=1)
        self.Description_label = customtkinter.CTkLabel(self.Description_frame, text="Test Hardware Description\nSetup Page",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.Description_label.grid(row=0, column=0, padx=30, pady=(50, 15))
        self.desc_operator_entry = customtkinter.CTkEntry(self.Description_frame, width=200, placeholder_text="Operator Name")#username
        self.desc_operator_entry.grid(row=1, column=0, padx=30, pady=(0, 15))
        self.desc_department_entry = customtkinter.CTkEntry(self.Description_frame, width=200, placeholder_text="Department i.e. Engineering")#username
        self.desc_department_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.desc_hardware_entry = customtkinter.CTkEntry(self.Description_frame, width=200, placeholder_text="Hardware Description")#username
        self.desc_hardware_entry.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.desc_serial_entry = customtkinter.CTkEntry(self.Description_frame, width=200, placeholder_text="Serial Number") 
        self.desc_serial_entry.grid(row=4, column=0, padx=30, pady=(0, 15))
        self.desc_assembly_entry = customtkinter.CTkEntry(self.Description_frame, width=200, placeholder_text="Assembly Number") #password #, show="*"
        self.desc_assembly_entry.grid(row=5, column=0, padx=30, pady=(0, 15))

        self.desc_login_button = customtkinter.CTkButton(self.Description_frame, text="Save Details", command=self.description_event, width=200)
        self.desc_login_button.grid(row=6, column=0, padx=30, pady=(15, 15))

        

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="CustomTkinter\nMain Page",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print("Login pressed - username:", self.username_entry.get(), "password:", self.password_entry.get())

        self.login_frame.grid_forget()  # remove login frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame
        
    def description_event(self):
        print("Description pressed - Assembly:", self.desc_assembly_entry.get(), "Operator:", self.desc_operator_entry.get())
        Operator  = self.desc_operator_entry
        Assembly = self.desc_assembly_entry
        serial = self.desc_serial_entry
        hardware = self.desc_hardware_entry
        department = self.desc_department_entry
        

        self.login_frame.grid_forget()  # remove login frame
        self.Description_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.login_frame.grid(row=0, column=0, sticky="ns")  # show login frame


if __name__ == "__main__":
    app = App()
    app.mainloop()