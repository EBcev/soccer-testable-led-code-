import time
import board
import neopixel
import tkinter as tk

# ---------------- LED SETTINGS ----------------

FIRST_PIN = board.D18
SECOND_PIN = board.D21

ICS_PER_STRIP = 6

FIRST_STRIPS = 50
SECOND_STRIPS = 20

FIRST_PIXELS = FIRST_STRIPS * ICS_PER_STRIP      # 300
SECOND_PIXELS = SECOND_STRIPS * ICS_PER_STRIP    # 120

BRIGHTNESS = 0.3

first_gpio = neopixel.NeoPixel(
    FIRST_PIN,
    FIRST_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRB
)

second_gpio = neopixel.NeoPixel(
    SECOND_PIN,
    SECOND_PIXELS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRB
)

# ---------------- LED SECTIONS ----------------

section_a_first = [2, 9, 10, 11, 12, 13, 14, 15, 16, 19, 48, 49, 50]
section_a_second = []

section_b_first = [1, 3, 4, 6, 7, 8, 17, 18, 20, 21, 47]
section_b_second = [1, 10, 11, 12, 14, 15, 16, 20]

section_c_first = [
    5, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46
]

section_c_second = [2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 19]

# ---------------- COLOURS ----------------

RED = (255, 0, 0)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# ---------------- LED FUNCTIONS ----------------

def set_one_strip(strip_object, strip_number, colour):
    start_ic = (strip_number - 1) * ICS_PER_STRIP

    for ic in range(start_ic, start_ic + ICS_PER_STRIP):
        strip_object[ic] = colour


def set_section(strip_object, strip_numbers, colour):
    for strip_number in strip_numbers:
        set_one_strip(strip_object, strip_number, colour)


def clear_all_leds():
    first_gpio.fill(OFF)
    second_gpio.fill(OFF)
    first_gpio.show()
    second_gpio.show()


def show_canada_flag_leds():
    first_gpio.fill(OFF)
    second_gpio.fill(OFF)

    # Canada flag: red, white, red
    set_section(first_gpio, section_a_first, RED)
    set_section(second_gpio, section_a_second, RED)

    set_section(first_gpio, section_b_first, WHITE)
    set_section(second_gpio, section_b_second, WHITE)

    set_section(first_gpio, section_c_first, RED)
    set_section(second_gpio, section_c_second, RED)

    first_gpio.show()
    second_gpio.show()

# ---------------- SCREEN FUNCTIONS ----------------

def show_canada_screen():
    root = tk.Tk()
    root.title("Country Display")

    # Fullscreen
    root.attributes("-fullscreen", True)

    # Red background
    root.configure(bg="red")

    label = tk.Label(
        root,
        text="CANADA",
        font=("Arial", 90, "bold"),
        fg="white",
        bg="red"
    )

    label.pack(expand=True)

    # Press ESC to exit
    root.bind("<Escape>", lambda event: close_program(root))

    root.mainloop()


def close_program(root):
    clear_all_leds()
    root.destroy()

# ---------------- MAIN PROGRAM ----------------

try:
    show_canada_flag_leds()
    print("Canada flag LEDs are on.")

    show_canada_screen()

except KeyboardInterrupt:
    clear_all_leds()
    print("LEDs off.")
