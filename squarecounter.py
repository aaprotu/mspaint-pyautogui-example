import pyautogui


class SquareCounter:
    def __init__(self):
        self.square_image = "square.png"

    def count_squares(self):
        # load the square template image
        template = pyautogui.locateOnScreen(self.square_image, grayscale=True)
        if template is None:
            return 0

        # count the number of squares using locateAll()
        squares = list(pyautogui.locateAllOnScreen(self.square_image, grayscale=True))
        return len(squares)