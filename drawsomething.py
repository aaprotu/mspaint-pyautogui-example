import pyautogui


class DrawSomething:
    def __init__(self):
        self.canvas_width = 1800
        self.canvas_height = 850

    # draw lines on squares
    def draw_some_lines(self):
        pyautogui.sleep(1)
        pyautogui.click(15, 150)
        while self.canvas_height > 0:
            if self.canvas_height - 100 < 0:
                break
            pyautogui.dragRel(self.canvas_width, 0, duration=0.0)  # right
            pyautogui.dragRel(0, 50, duration=0.0)  # down
            self.canvas_height -= 50
            pyautogui.dragRel(-self.canvas_width, 0, duration=0.0)  # left
            pyautogui.dragRel(0, 50, duration=0.0)  # down
            self.canvas_height -= 50
