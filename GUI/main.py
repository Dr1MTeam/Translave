
import customtkinter
import customtkinter as ctk

import webbrowser

from PIL import Image, ImageSequence

import threading as th
import time

ctk.set_default_color_theme("Themes/TransLave.json")
ctk.set_appearance_mode("dark")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.theme = 0
        self.geometry("1080x720")
        self.title('Translave')

        container = ctk.CTkFrame(self)
        container.pack(side="top", fill="both", expand=True)

        self.minsize(720, 720)
        self.frames = {}

        for F in (MainWindow, SettingsWindow):
            page_name = F.__name__

            frame = F(parent=container)
            print(frame)
            self.frames[page_name] = frame
            frame.grid(column=0, row=0, sticky="nsew")
        self.draw_header()

    def draw_header(self):

        header_frame = ctk.CTkFrame(self)
        header_frame.configure(fg_color=( "#ffa667", "#1e222d",))
        header_frame.place(
            x=0, y=0,
            relwidth=1, relheight=0.15)
        header_frame.columnconfigure((0, 1, 2, 3), weight=1)

        header_frame.rowconfigure((0), weight=1)
        font = ctk.CTkFont(family="Konstanting", size=70)
        title_text = ctk.CTkLabel(
            header_frame,
            text="TRANSLAVE", font=font
        )

        title_text.grid(
            row=0, column=0,
            padx=50, pady=20,
            sticky='nswe')

        theme = ctk.StringVar(value="light")

        def switch_theme_event():

            if theme.get() == "dark":
                ctk.set_appearance_mode("dark")
                theme.set("light")
            else:
                ctk.set_appearance_mode("light")
                theme.set("dark")

        theme_switch_button = ctk.CTkButton(
                header_frame,
                corner_radius=15,
                command=switch_theme_event).grid(row=0, column=2,
                                         padx=5, pady=10,
                                         sticky='nswe')

        header_value = ctk.StringVar(value="MainWindow")

        def show_frame():
            frame = self.frames[header_value.get()]
            print(frame)
            frame.tkraise()
            if header_value.get() == "MainWindow":
                header_value.set("SettingsWindow")
            else:
                header_value.set("MainWindow")
        settings_button = ctk.CTkButton(header_frame, text='settings', command=show_frame)

        settings_button.grid(
            row=0, column=3,
            padx=10, pady=10,
            sticky='nswe', )

        def callback():
            webbrowser.open_new(r"https://github.com/Dr1MTeam/Translave")

        "InfoBottomText"

        bottom_info_frame = ctk.CTkFrame(self)
        bottom_info_frame.place(x=0, rely=0.95,
            relwidth=1, relheight=0.05)

        bottom_info_frame.columnconfigure(0, weight=1)
        bottom_info_frame.configure(fg_color=("#ffa667", "#1e222d",))

        text_info = ctk.CTkButton(bottom_info_frame, text="@Dr1mTeam/TransLave",
                                  command=callback,  fg_color=("#ffa667", "#1e222d",))
        text_info.grid(column=1, row=0, sticky="nse", padx=15, pady=5)


class MainWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        "HeaderFrame"

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.place(
            x=0, rely=0.15,
            relwidth=1, relheight=0.80)

        "MainFrame"

        self.main_frame.columnconfigure((0,1), weight=1)
        self.main_frame.rowconfigure((0,1), weight=1)

        self.text_translation = ctk.CTkTextbox(self.main_frame, activate_scrollbars=True)
        self.text_translation.grid(
            row=0, column=0,
            padx=10, pady=30,
            rowspan=1, sticky='nswe',)
        self.text_to_translate = ctk.CTkTextbox(self.main_frame,activate_scrollbars=True)
        self.text_to_translate.grid(
            row=0, column=1,
            padx=10, pady=30,
            rowspan=1, sticky='nswe',)




class SettingsWindow(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)

        self.main_frame = ctk.CTkFrame(self)

        parent.grid_columnconfigure(0,  weight=1)
        parent.grid_rowconfigure(0, weight=1)

        self.main_frame.place(
            x=0, rely=0.15,
            relwidth=1, relheight=0.80)

        option_menu_var = customtkinter.StringVar(value="MT5-translave")

        def switch_ml(choice):
            print("model switched to ", choice)
            " Здесь часть программы с изменением модели"


        self.ml_label = ctk.CTkLabel(self.main_frame, text="Выбор модели перевода:")
        self.ml_label.grid(
            row=0, column=1, padx=40, pady=30, sticky='nswe',
        )

        self.ml_switch_btn_1 = ctk.CTkOptionMenu(self.main_frame,
                                                 values=["MT5 ", "Mt5-translave"],
                                                 command=switch_ml,
                                                 variable=option_menu_var
        )

        self.ml_switch_btn_1.grid(
            row=0, column=2, padx=0, pady=30, sticky='nswe',
        )

        def switch_input():
            print("model switched")
            " Здесь часть программы с переключением типа ввода"


        def unpack_gif(src):
            # Load Gif
            image = Image.open(src)

            # Get frames and disposal method for each frame
            frames = []
            disposal = []
            for gifFrame in ImageSequence.Iterator(image):
                disposal.append(gifFrame.disposal_method)
                frames.append(gifFrame.convert('P'))
            print(frames)
            # Loop through frames, and edit them based on their disposal method
            output = []
            lastFrame = None
            thisFrame = None
            for i, loadedFrame in enumerate(frames):
                # Update thisFrame
                print(loadedFrame)
                thisFrame = loadedFrame

                # If the disposal method is 2
                if disposal[i] == 2:
                    # Check that this is not the first frame
                    if i != 0:
                        # Pastes thisFrames opaque pixels over lastFrame and appends lastFrame to output
                        lastFrame.paste(thisFrame, mask=thisFrame.convert('RGBA'))
                        output.append(lastFrame)
                    else:
                        output.append(thisFrame)

                # If the disposal method is 1 or 0
                elif disposal[i] == 1 or disposal[i] == 0:
                    # Appends thisFrame to output
                    output.append(thisFrame)

                # If disposal method if anything other than 2, 1, or 0
                else:
                    raise ValueError(
                        'Disposal Methods other than 2:Restore to Background, 1:Do Not Dispose, and 0:No Disposal are supported at this time')

                # Update lastFrame
                lastFrame = loadedFrame

            return output

        imgr = unpack_gif("GUI_images/VolcanoGif.gif")
        self.volcano_button = ctk.CTkButton(self.main_frame, text="",)

        def gif(img):
            time.sleep(0.28)
            while True:

                for i, frame in enumerate(img[2:]):
                    self.main_frame.update()
                    self.volcano_button.configure(self.main_frame,
                                                  anchor=(0,0),
                                                  fg_color=("#ff9300", "#464a55",),
                                                  state="disabled",
                                                  image=ctk.CTkImage(light_image=frame,
                                                                     dark_image=frame,
                                                                     size=(420, 480)))

                    self.main_frame.update()

                    print(frame, i)
                    time.sleep(0.16)

        a = th.Thread(daemon=True, target=gif,args=[imgr])
        a.start()
        self.main_frame.columnconfigure(3, weight=1)
        self.main_frame.rowconfigure(1, weight=1)
        self.volcano_button.grid(row=1, column=3, sticky="se")


if __name__ == "__main__":
    app = App()

    app.mainloop()
