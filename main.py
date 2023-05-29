import random
import pyautogui
from paint import Paint
from draw import Draw
from squarecounter import SquareCounter
from drawsomething import DrawSomething


def main():
    paint = Paint()
    paint.open()

    print("Starting to draw...")

    draw = Draw()
    num_squares = random.randint(2, 5)
    draw.draw_squares(num_squares)

    print(str(num_squares) + " squares drawn.")

    square_counter = SquareCounter()
    counted_squares = square_counter.count_squares()

    print("Counting the squares...")

    if counted_squares == num_squares:
        print("Square counting successful. " + str(counted_squares) + " squares found.")
    else:
        print("Square counting failed. " + str(counted_squares) + " squares found.")

    print("Drawing something on canvas...")

    drawrandom = DrawSomething()
    drawrandom.draw_some_lines()

    print("Counting the squares again...")

    counted_squares = square_counter.count_squares()
    if counted_squares == 0:
        print(str(counted_squares) + " squares found.")

    pyautogui.hotkey("alt", "f4")
    pyautogui.sleep(1)
    pyautogui.hotkey("n")


if __name__ == "__main__":
    main()
