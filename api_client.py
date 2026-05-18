
import json
from nba_api.live.nba.endpoints import scoreboard, boxscore

HEADERS = { # cus nba blocks requests w/o browser header :(
    "Host": "cdn.nba.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Origin": "https://www.nba.com",
    "Referer": "https://www.nba.com/",
    "Connection": "keep-alive",
}

def get_live_game_ids():
    """Returns list of game IDs that are currently in progress."""
    board = scoreboard.ScoreBoard(headers=HEADERS)
    games = board.get_dict()["scoreboard"]["games"]

    print("\n=== ALL GAMES TODAY ===")
    for g in games:
        status = {1: "Scheduled", 2: "LIVE", 3: "Final"}.get(g["gameStatus"], "Unknown")
        print(f"  [{status}] {g['awayTeam']['teamTricode']} @ {g['homeTeam']['teamTricode']} — ID: {g['gameId']}")

    live = [g["gameId"] for g in games if g["gameStatus"] == 2]
    print(f"\n  {len(live)} live game(s) found\n")
    return live

def get_team_scores(game_id: str) -> dict:
    box = boxscore.BoxScore(game_id=game_id, headers=HEADERS).get_dict()["game"]
    home = box["homeTeam"]
    away = box["awayTeam"]

    result = {
        "home": {
            "name": f"{home['teamCity']} {home['teamName']}",
            "tricode": home["teamTricode"],
            "score": home["score"],
        },
        "away": {
            "name": f"{away['teamCity']} {away['teamName']}",
            "tricode": away["teamTricode"],
            "score": away["score"],
        }
    }

    print(f"=== BOXSCORE: {result['away']['tricode']} @ {result['home']['tricode']} ===")
    print(json.dumps(result, indent=2))
    print()

    return result