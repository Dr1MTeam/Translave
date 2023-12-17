import pyscreenshot
import os
from pynput import mouse
import keyboard


def on_click(x, y, button, pressed, new_arr=(0, 0)):
    if pressed:
        print('start', x, y)
        new_arr = (x, y)
        arr[0] = new_arr[0]
        arr[1] = new_arr[1]

    else:
        print('end', x, y)
        new_arr = (x, y)
        arr[2] = new_arr[0]
        arr[3] = new_arr[1]
    if not pressed:
        print('screenshot mod deactivated')
        print(arr[0], arr[1], arr[2], arr[3])

        try:
            if arr[0] <= arr[2] and arr[1] <= arr[3]:
                print('type 1 : x1 <= x2 and y1 <= y2')
                image = pyscreenshot.grab(bbox=(arr[0], arr[1], arr[2], arr[3]))

            elif arr[0] <= arr[2] and arr[1] >= arr[3]:
                print('type 2 : x1 <= x2 y1 >= y2')
                image = pyscreenshot.grab(bbox=(arr[0], arr[3], arr[2], arr[1]))

            elif arr[0] >= arr[2] and arr[1] <= arr[3]:

                print('type 3 : x1 >= x2 y1 <= y2')
                image = pyscreenshot.grab(bbox=(arr[2], arr[1], arr[0], arr[3]))

            elif arr[0] >= arr[2] and arr[1] >= arr[3]:

                print('type 4 : x1 >= x2 y1 >= y2')
                image = pyscreenshot.grab(bbox=(arr[2], arr[3], arr[0], arr[1]))

            image.show(path)
            image.save(path)

        except Exception:
            print("Ошибка при создании скриншота")

        finally:
            return False


class ScreenShotApp:
    def __init__(self):
        self.hot_key = 'ctrl+p'

    def clear_images(self):
        if os.path.exists(path):
            os.remove(path)
            print("folder images is clear")
        else:
            print('folder is empty')

    def change_hot_key(self):
        pass

    def screenshot_activate(self):
        self.clear_images()
        print('screenshot mod activate')
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

    def start(self):
        keyboard.add_hotkey(self.hot_key, self.screenshot_activate)
        keyboard.wait()


arr = [0, 0, 0, 0]
path = r"assets\new.png"
app = ScreenShotApp()
app.start()




