import pyautogui


class Paint:
    def __init__(self):
        self.app_name = "mspaint"
        self.canvas_width = 1900
        self.canvas_height = 800

    def open(self):
        pyautogui.hotkey("win", "r")
        pyautogui.write(self.app_name)
        pyautogui.press("enter")

        # wait until mspaint is running
        pyautogui.sleep(1)

        # maximize window
        pyautogui.hotkey("win", "up")
        pyautogui.sleep(1)
