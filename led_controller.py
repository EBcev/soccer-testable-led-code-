# src/led_controller.py
from config import LED_BRIGHTNESS

def trigger_update(update: dict):
    """
    Called whenever a team scores.
    
    `update` contains:
        - team         : full team name e.g. "Boston Celtics"
        - tricode      : short code e.g. "BOS"
        - score        : their new total score e.g. 56
        - points_scored: how many points this basket was worth (1, 2, or 3)
    
    Fill in the below accordingly, variables have been created for use
    """
    team          = update["team"]
    tricode       = update["tricode"]
    score         = update["score"]
    points_scored = update["points_scored"]

    print(f"[LED] {team} ({tricode}) scored {points_scored}pts — now at {score}") # for testing, replace this

    # ---- Neopixel code goes here ----
