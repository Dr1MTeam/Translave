import tkinter as tk
from tkinter import ttk

import customtkinter
#from ttkbootstrap import *
import customtkinter as ctk
import pathlib, os
import glob
from PIL import ImageTk, Image
CURRENT_PATH = pathlib.Path(__file__).parent.resolve()
RELATIVE_ASSETS_PATH = "../frame0/"


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.geometry("1080x720")
        self.title('Translave')

        container = ctk.CTkFrame(self)
        container.pack(side="top",fill="both", expand=True)

        self.minsize(720, 536)
        # self.main_frame = MainWindow(parent=self)
        # self.main_frame.grid(row=0, column=0, sticky="nwse")

        self.frames = {}
        for F in (MainWindow, SettingWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame("MainWindow")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent, controller):
        "HeaderFrame"
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller
        self.header_frame = ttk.Frame(self)
        self.main_frame = ttk.Frame(self)
        self.bottom_info_frame = ttk.Frame(self)

        self.header_frame.place(
            x=0, y=0,
            relwidth=1, relheight=0.15)
        self.main_frame.place(
            x=0, rely=0.15,
            relwidth=1, relheight=0.80)
        self.bottom_info_frame.place(
            x=0, rely=0.95,
            relwidth=1, relheight=0.05)

        self.header_frame.columnconfigure((0,1,2,3), weight=1)

        self.header_frame.rowconfigure((0), weight=1)

        self.title_text = ctk.CTkLabel(
            self.header_frame,
            text="TRANSLAVE",text_color=("Red","BLACK")
        )

        self.title_text.grid(
            row=0, column=0,
            padx=50, pady=20,
            sticky='nswe')

        self.settings_button = ctk.CTkButton(self.header_frame, text='settings',
                                             command=lambda: controller.show_frame("SettingWindow"))
        self.settings_button.grid(
            row=0,  column=3,
            padx=10,pady=10,
            sticky='nswe',)

        """SwitchThemes"""


        switch_var = ctk.IntVar(value=1)

        def switch_event():
            ctk.set_appearance_mode("light") if switch_var.get() else ctk.set_appearance_mode("dark")
            switch_var.set(not switch_var.get())


        self.theme_switch_image = ctk.CTkImage(Image.open('../frame0/button_1.png'), size=(150, 70))

        self.theme_switch_button = ctk.CTkButton(
            self.header_frame,
            corner_radius=15,

            fg_color=("#FFFF00", "#0000FF"),
            command=switch_event).grid(row=0, column=2,
                                     padx=5, pady=10,
                                     sticky='nswe')

        "MainFrame"

        self.main_frame.columnconfigure((0,1), weight=1)
        self.main_frame.rowconfigure((0), weight=1)

        self.text_translation = ctk.CTkTextbox(self.main_frame,activate_scrollbars=True)
        self.text_translation.grid(
            row=0, column=0,
            padx=10, pady=30,
            rowspan=1, sticky='nswe',)
        self.text_to_translate = ctk.CTkTextbox(self.main_frame,activate_scrollbars=True)
        self.text_to_translate.grid(
            row=0,column=1,
            padx=10, pady=30,
            rowspan=1, sticky='nswe',)

        "InfoBottomText"
        self.bottom_info_frame.columnconfigure((0,1), weight=1)

        self.text_info = ctk.CTkLabel(self.bottom_info_frame, text="@DreamTeam/Translave", text_color="#FF00FF")
        self.text_info.grid(column=1, row=0, sticky="nse", padx=15)


class SettingWindow(ctk.CTkFrame):
    def __init__(self, parent, controller):
        "HeaderFrame"
        ctk.CTkFrame.__init__(self, parent)
        self.controller = controller

        self.header_frame = ttk.Frame(self)
        self.main_frame = ttk.Frame(self)
        self.bottom_info_frame = ttk.Frame(self)
        parent.grid_columnconfigure(0, weight=1)
        parent.grid_rowconfigure(0, weight=1)
        self.header_frame.place(
            x=0, y=0,
            relwidth=1, relheight=0.15)
        self.main_frame.place(
            x=0, rely=0.15,
            relwidth=1, relheight=0.80)
        self.bottom_info_frame.place(
            x=0, rely=0.95,
            relwidth=1, relheight=0.05)
        self.header_frame.columnconfigure((0, 1, 2, 3), weight=1)

        self.header_frame.rowconfigure((0), weight=1)

        self.title_text = ctk.CTkLabel(
            self.header_frame,
            text="TRANSLAVE", text_color=("Red", "BLACK")
        )

        self.title_text.grid(
            row=0, column=0,
            padx=50, pady=20,
            sticky='nswe')

        self.return_button = ctk.CTkButton(self.header_frame, text='return',
                                             command=lambda: controller.show_frame("MainWindow"))
        self.return_button.grid(
            row=0, column=3,
            padx=10, pady=10,
            sticky='nswe', )

        switch_var = ctk.IntVar(value=1)

        def switch_event():
            ctk.set_appearance_mode("light") if switch_var.get() else ctk.set_appearance_mode("dark")
            switch_var.set(not switch_var.get())

        self.theme_switch_button = ctk.CTkButton(
            self.header_frame,
            corner_radius=15,

            fg_color=("#FFFF00", "#0000FF"),
            command=switch_event).grid(row=0, column=2,
                                       padx=5, pady=10,
                                       sticky='nswe')
        ml_model_var = ctk.IntVar(0)
        def switch_ml():
            print("model switched")
            " Здесь часть программы с изменением модели"

        self.ml_switch_btn_1 = ctk.CTkRadioButton(self.main_frame,
                                              text="модель А",
                                              command=switch_ml(),
                                              variable=ml_model_var,
                                              value=0,
                                              text_color=("#000000", "red"))
        self.ml_switch_btn_1.grid(
            row=0, column=1, padx=120, pady=10, sticky='nswe',
        )
        self.ml_switch_btn_2 = ctk.CTkRadioButton(self.main_frame,
                                              text="модель Б",
                                              command=switch_ml(),
                                              variable=ml_model_var,
                                              value=1,
                                              text_color=("#000000", "red"))
        self.ml_switch_btn_2.grid(
            row=1,  column=1, padx=120, pady=10, sticky='nswe',
        )

        input_action_var = ctk.IntVar(0)
        def switch_ml():
            print("model switched")
            " Здесь часть программы с переключением типа ввода"

        self.input_switch_btn_1 = ctk.CTkRadioButton(self.main_frame,
                                                     text="Ввод 1",
                                                     command=switch_ml(),
                                                     variable=input_action_var,
                                                     value=0,
                                                     text_color=("#000000", "red"))
        self.input_switch_btn_2 = ctk.CTkRadioButton(self.main_frame,
                                                     text="Ввод 2",
                                                     command=switch_ml(),
                                                     variable=input_action_var,
                                                     value=1,
                                                     text_color=("#000000", "red"))

        self.input_switch_btn_1.grid(
            row=0,  column=2, padx=60, pady=10, sticky='nswe',
        )
        self.input_switch_btn_2.grid(
            row=1,  column=2, padx=60, pady=10, sticky='nswe',
        )


if __name__ == "__main__":
    app = App()
    app.mainloop()
