from typing import Literal
from config.settings import SETTINGS

Tone = Literal["neutral", "viral", "analysis"]

def to_lower(text: str) -> str:
    if getattr(SETTINGS, "lowercase_posts", False):
        return text.lower()
    return text


def build_post_variants(insight: str, tone: Tone = "neutral") -> dict:
    """
    Generates X / social media post variants from a sports insight.
    """

    neutral = f"""
observation
{insight}

mechanism
games shift when one hidden edge tilts the environment.

implication
if the edge holds, the scoreboard usually follows.
"""

    viral = f"""
fans see the scoreboard

frame² sees the edge

{insight}
"""

    analysis = f"""
observation
{insight}

mechanism
contact quality
plate discipline
run expectancy swings

implication
process eventually beats variance.
"""

    posts = {
        "neutral": to_lower(neutral.strip()),
        "viral": to_lower(viral.strip()),
        "analysis": to_lower(analysis.strip()),
    }

    return posts
