import time
from src.led_controller import trigger_update
import tkinter as tk
from rpi_ws281x import PixelStrip, Color

timeToWait = 5 # adjust this for testing speed, in seconds

# LED SETTINGS 

LED_COUNT = 60
LED_PIN = 18          # GPIO18, physical pin 12
LED_BRIGHTNESS = 204  # around 80%

strip = PixelStrip(LED_COUNT, LED_PIN, brightness=LED_BRIGHTNESS)
strip.begin()

TEAM_A_COLOUR = Color(0, 255, 0)      # green
TEAM_B_COLOUR = Color(128, 0, 255)    # purple

def set_strip_colour(colour):
    for i in range(LED_COUNT):
        strip.setPixelColor(i, colour)
    strip.show()

def clear_strip():
    for i in range(LED_COUNT):
        strip.setPixelColor(i, Color(0, 0, 0))
    strip.show()

# SCORE POPUP SCREEN 

root = tk.Tk()
root.title("Live Score")
root.geometry("400x200")

score_label = tk.Label(
    root,
    text="Waiting for score...",
    font=("Arial", 28),
    padx=20,
    pady=20
)

score_label.pack(expand=True)


def update_score_screen(scoring_team, score_a, score_b):
    score_text = (
        f"{scoring_team['team']} scored!\n\n"
        f"{TEAM_A['tricode']} {score_a} - {TEAM_B['tricode']} {score_b}"
    )

    score_label.config(text=score_text)
    root.update()

# TEAM LABELS
TEAM_A = {"team": "Boston Celtics", "tricode": "BOS"}
TEAM_B = {"team": "Los Angeles Lakers", "tricode": "LAL"}

score_a = 0
score_b = 0
turn = 0

print("LED Test  simulating live game, Ctrl+C to stop\n")

# MAIN 

while True:
    if turn % 2 == 0:
        score_a += 2
        update = {
            "team": TEAM_A["team"],
            "tricode": TEAM_A["tricode"],
            "score": score_a,
            "points_scored": 2,
        }
        scoring_team = TEAM_A
        set_strip_colour(TEAM_A_COLOUR)

    else:
        score_b += 2
        update = {
            "team": TEAM_B["team"],
            "tricode": TEAM_B["tricode"],
            "score": score_b,
            "points_scored": 2,
        }
        scoring_team = TEAM_B
        set_strip_colour(TEAM_B_COLOUR)

    trigger_update(update)
    print(f"  Score: {TEAM_A['tricode']} {score_a} — {TEAM_B['tricode']} {score_b}\n")
    update_score_screen(scoring_team, score_a, score_b)

    turn += 1
    time.sleep(timeToWait) 