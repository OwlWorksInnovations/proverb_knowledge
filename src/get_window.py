import tkinter as tk

def get_window_size():
    # Initialize tkinter
    root = tk.Tk()

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # The bottom-right coordinate is (screen_width, screen_height)
    bottom_right = (screen_width, screen_height)

    return screen_width, screen_height

    # Close the tkinter root
    root.destroy()
