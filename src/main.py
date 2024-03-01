import pyautogui
import time
import keyboard


def auto_clicker(interval):
    try:
        while True:
            # If "`" key is pressed, start/stop clicking
            if keyboard.is_pressed('space'):
                position = pyautogui.position()  # Clicks where the mouse pointer is
                time.sleep(0.5)  # Adding sleep to prevent immediate toggle on key press
                while not keyboard.is_pressed('space'):
                    print("Clicking at position: " + str(position))
                    pyautogui.click(position)
                    # time.sleep(interval)
                time.sleep(0.5)  # Adding sleep to prevent immediate toggle on key press
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")


if __name__ == "__main__":
    print("Press [space] to start clicking. Press [space] again to stop.")
    try:
        auto_clicker(interval=0.0001)
    except KeyboardInterrupt:
        print("\nAuto-clicker stopped.")
