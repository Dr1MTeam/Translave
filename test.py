import pyscreenshot
import os
from pynput import mouse
import keyboard
import easyocr
from tkinter import *

import os, time

class TextRecognition:

    def __init__(self):
        self.res = ""

    def text_recognition(self, file_path):

        reader = easyocr.Reader(["ru", "en"])
        result = reader.readtext(file_path, detail=0)
        res_string = ""
        for i in result:
            res_string += i + ' '

        self.res = res_string
        return self.res
        #print(self.res)

    def get_res(self):
        return self.res

    def set_res(self, result):
        self.res = result

class ScreenShotApp:

    def __init__(self):
        self.path = r"assets\new.png"
        self.arr = [0, 0, 0, 0]
        self.res = ""

    def clear_images(self):
        if os.path.exists(self.path):
            os.remove(self.path)
            print("folder images is clear")
        else:
            print('folder is empty')

    def change_hot_key(self):
        self.hot_key = input()

    def screenshot_activate(self):
        self.clear_images()
        print('screenshot mod activate')
        with mouse.Listener(on_click=self.on_click) as listener:
            listener.join()

    def on_click(self, x, y, button, pressed, new_arr=(0, 0)):
        if pressed:
            print('start', x, y)
            new_arr = (x, y)
            self.arr[0] = new_arr[0]
            self.arr[1] = new_arr[1]

        else:
            print('end', x, y)
            new_arr = (x, y)
            self.arr[2] = new_arr[0]
            self.arr[3] = new_arr[1]
        if not pressed:
            print('screenshot mod deactivated')
            print(self.arr[0], self.arr[1], self.arr[2], self.arr[3])

            try:
                image = None
                if self.arr[0] <= self.arr[2] and self.arr[1] <= self.arr[3]:
                    print('type 1 : x1 <= x2 and y1 <= y2')
                    image = pyscreenshot.grab(bbox=(self.arr[0], self.arr[1], self.arr[2], self.arr[3]))

                elif self.arr[0] <= self.arr[2] and self.arr[1] >= self.arr[3]:
                    print('type 2 : x1 <= x2 y1 >= y2')
                    image = pyscreenshot.grab(bbox=(self.arr[0], self.arr[3], self.arr[2], self.arr[1]))

                elif self.arr[0] >= self.arr[2] and self.arr[1] <= self.arr[3]:

                    print('type 3 : x1 >= x2 y1 <= y2')
                    image = pyscreenshot.grab(bbox=(self.arr[2], self.arr[1], self.arr[0], self.arr[3]))

                elif self.arr[0] >= self.arr[2] and self.arr[1] >= self.arr[3]:

                    print('type 4 : x1 >= x2 y1 >= y2')
                    image = pyscreenshot.grab(bbox=(self.arr[2], self.arr[3], self.arr[0], self.arr[1]))

                image.save(self.path)
                #TextRecognition().text_recognition(self.path)

            except Exception:

                print("Ошибка при создании скриншота")

            finally:
                return False



# app = ScreenShotApp()
# app.start()

