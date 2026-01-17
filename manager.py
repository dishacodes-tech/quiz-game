import json
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
score_file = os.path.join(BASE_DIR, "score.json")


def load_high_score():
    if not os.path.exists(score_file):
        data = {"high_score": 0, "score_date": None}
        with open(score_file, "w") as f:
            json.dump(data, f, indent=4)
        return 0, None

    try:
        with open(score_file, "r") as f:
            data = json.load(f)
            return data.get("high_score", 0), data.get("score_date", None)

    except json.JSONDecodeError:
        return 0, None


def save_high_score(score):
    data = {
        "high_score": score,
        "score_date": datetime.now().strftime("%d-%m-%Y")
    }
    with open(score_file, "w") as f:
        json.dump(data, f, indent=4)