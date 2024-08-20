import pyautogui
import time

def scroll_slow_down():
    pyautogui.scroll(-50)  # Slow scroll down

def scroll_slow_up():
    pyautogui.scroll(50)  # Slow scroll up

def scroll_fast_down(Accel):
    Accel = 1.5
    tdelay = Accel*0.025
    sdisp = Accel*25
    for i in range(0,20):
        pyautogui.vscroll(sdisp)  # Fast and longer scroll up
        time.sleep(tdelay)

def scroll_fast_up(Accel):
    Accel = 1.5
    tdelay = Accel*0.025
    sdisp = Accel*25
    for i in range(0,20):
        pyautogui.vscroll(sdisp)  # Fast and longer scroll up
        time.sleep(tdelay)

# Independent functions for movement
def move_left():
    pyautogui.press('left')  # Move left with left arrow key

def move_right():
    pyautogui.press('right')  # Move right with right arrow key

# Independent functions for zooming
def zoom_in():
    pyautogui.hotkey('ctrl', '+')  # Zoom in

def zoom_out():
    pyautogui.hotkey('ctrl', '-')  # Zoom out


def open_file(file_position):
    pyautogui.doubleClick(file_position)  # Double-click on the file at the given position
    time.sleep(2)  # Wait for the file to open

# Function to scroll up and down
def scroll_file(scroll_up, scroll_down, wait_time):
    pyautogui.scroll(scroll_up)  # Scroll up
    time.sleep(wait_time)  # Wait for specified time
    pyautogui.scroll(scroll_down)  # Scroll down
    time.sleep(wait_time)
    pyautogui.scroll(scroll_up)  # Scroll down
    time.sleep(wait_time)

# Function to close the file
def close_file():
    pyautogui.hotkey('ctrl', 'w')  # Close the file (works in many applications)
    time.sleep(2)  # Wait for the file to close

file_position = (509, 308)  # (x, y) coordinates of the file

#open_file(file_position)

# Scroll up, wait 2 seconds, and then scroll down
def main(input_from_gyroscope):
    if input_from_gyroscope == "scroll_slow_down":
        scroll_slow_down()
    elif input_from_gyroscope == "scroll_slow_up":
        scroll_slow_up()
    elif input_from_gyroscope == "scroll_fast_down":
        scroll_fast_down()
    elif input_from_gyroscope == "scroll_fast_up":
        scroll_fast_up()
    elif input_from_gyroscope == "move_left":
        move_left()
    elif input_from_gyroscope == "move_right":
        move_right()
    elif input_from_gyroscope == "zoom_in":
        zoom_in()
    elif input_from_gyroscope == "zoom_out":
        zoom_out()
    elif input_from_gyroscope == "open_file":
        file_path = input("Enter the file path to open: ")
        open_file(file_path)
    elif input_from_gyroscope == "close_file":
        window_title = input("Enter the window title to close: ")
        close_file(window_title)
    else:
        print("Invalid input")

# Example usage
if __name__ == "__main__":
    # Simulated input from gyroscope
    time.sleep(2)
    open_file(file_position)
    time.sleep(3)
    input_from_gyroscope = "scroll_fast_up"
    main(input_from_gyroscope)
    time.sleep(3)
    input_from_gyroscope = "scroll_fast_down"
    main(input_from_gyroscope)
    time.sleep(3)
    zoom_in()
    time.sleep(3)
    zoom_out()
    time.sleep(3)
    #input_from_gyroscope = "scroll_fast_up"
    close_file()