class ScoreTracker:
    def __init__(self):
        self.last_scores = {}
        # { gameId: { "home": { "name": ..., "tricode": ..., "score": 0 },
        #             "away": { "name": ..., "tricode": ..., "score": 0 } } }

    def check_for_updates(self, game_id: str, current: dict) -> list[dict]:
        """
        Compares current scores against last known scores.
        Returns a list of teams that just scored, empty list if no change.

        Each update looks like:
        { "team": "Boston Celtics", "tricode": "BOS", "score": 12 }
        """
        updates = []
        prev = self.last_scores.get(game_id)

        if prev is None:
            # First time seeing this game, just store and move on
            print(f"  [tracker] First seen: {current['away']['tricode']} @ {current['home']['tricode']} — storing initial scores")
            self.last_scores[game_id] = current
            return []

        for side in ("home", "away"):
            curr_score = current[side]["score"]
            prev_score = prev[side]["score"]
            team_name  = current[side]["name"]
            tricode    = current[side]["tricode"]

            if curr_score > prev_score:
                updates.append({
                    "team":   team_name,
                    "tricode": tricode,
                    "score":  curr_score,
                    "points_scored": curr_score - prev_score,  # 1, 2, or 3
                })
                print(f"  [tracker] SCORE: {team_name} ({tricode}) now at {curr_score} (+{curr_score - prev_score})")

        self.last_scores[game_id] = current
        return updates