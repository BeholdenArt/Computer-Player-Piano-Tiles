import pyautogui
import mss
import time


def click():
    with mss.mss() as sct:
        while True:
            img = sct.grab(bbox)    # Taking Screenshot

            for coordinate in coordinate_x:
                if img.pixel(coordinate, 0)[0] < 100:    # Checking black & blue pixels
                    pyautogui.click(INITIAL_X + coordinate, INITIAL_Y)    # Click
                    break

if __name__ == "__main__":
    time.sleep(4)
    INITIAL_X, INITIAL_Y = 660, 650    # Boundaries of game window
    bbox = (INITIAL_X, INITIAL_Y, INITIAL_X+540, INITIAL_Y+1)

    coordinate_x = [0, 180, 360, 539]    # Lanes of tiles (4)
    click()
