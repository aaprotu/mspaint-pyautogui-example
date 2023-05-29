import pyautogui
import random


class Draw:
    def __init__(self):
        self.canvas_width = 1850
        self.canvas_height = 850
        self.square_size = 150

    # check that the area around coordinates contains
    # only white pixels
    def is_area_white(self, x, y, size):
        screenshot = pyautogui.screenshot(region=(x, y, size, size))
        for i in range(size):
            for j in range(size):
                pixel = screenshot.getpixel((i, j))
                if pixel != (255, 255, 255):
                    return False
        return True

    def draw_squares(self, num_squares):
        for _ in range(num_squares):
            # generate random x,y positions
            while True:
                x = random.randint(0, self.canvas_width)
                y = random.randint(0, self.canvas_height)
                if self.is_area_white(x, y, self.square_size):
                    break

            pyautogui.moveTo(x, y)
            pyautogui.dragRel(self.square_size, 0)
            pyautogui.dragRel(0, self.square_size)
            pyautogui.dragRel(-self.square_size, 0)
            pyautogui.dragRel(0, -self.square_size)
