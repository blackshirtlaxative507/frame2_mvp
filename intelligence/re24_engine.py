from __future__ import annotations

import pandas as pd

RUN_EXPECTANCY = {
    (0, 0): 0.54, (1, 0): 0.95, (2, 0): 1.19, (3, 0): 1.48,
    (0, 1): 0.29, (1, 1): 0.57, (2, 1): 0.73, (3, 1): 0.98,
    (0, 2): 0.11, (1, 2): 0.24, (2, 2): 0.35, (3, 2): 0.39,
}


def estimate_re24_delta(runners_on: int, outs: int, next_runners_on: int, next_outs: int) -> float:
    start = RUN_EXPECTANCY.get((runners_on, outs), 0.0)
    end = RUN_EXPECTANCY.get((next_runners_on, next_outs), 0.0)
    return round(end - start, 3)


def summarize_re24_proxy(df: pd.DataFrame) -> float:
    if df.empty:
        return 0.0

    if "events" not in df.columns:
        return 0.0

    positive_events = {"single", "double", "triple", "home_run", "walk", "hit_by_pitch"}
    negative_events = {"strikeout", "grounded_into_double_play"}

    score = 0.0
    for event in df["events"].dropna().astype(str):
        if event in positive_events:
            score += 0.35
        elif event in negative_events:
            score -= 0.25

    return r    return r    return r intelligence/tilt_detector.py <<'EOF'
from __futurefrom __futurefrom __futurefrom __futurefrom __futurefrom _
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@te_good: float = 0.08
    hard_hit_rate_good: float = 0.40
    cha    cha    cha    cha    cha    cha    cha    cha    cha    cha    cha    cha    cha    cha    ch24_swing_good: float = 1.00


@dataclass
class TiltDetector:
    thresholds: TiltThresholds = TiltThresholds()

    def full_tilt_read(
        self,
        barrel_rate: float,
        chase_rate: float,
        whiff_rate: float,
        re24_change: float,
        hard_hit_rate:         hard_hit_           hard_hit_rate:         hard_hit_           hard_hit_rate:         hard_hit_    te        hard_hit_rate:         hard_hit_           hard_hit_rathre        hard_ht_rate_good:
            contact_quality = "contact qu            contact_quality = "contnd            contact_qua               contact_quality = "conta"no            contact_qual        if chase_rate <= self.thresholds.chase_rate_good and whiff_rate <= sel            contact_quality = "contact qu            contact_quality =t"            contact_quality = "contact qu            contact_quality = "contnd"no            contact_qual   if re24_change >= self.thresholds.re24_swing_good or xwoba >= self.thresholds.xwoba_good:
            run_environment = "run environment tilt"
                              en                              en                men            environment tilt"

                                 = 1 if contact_quality != "no contact quality tilt" else 0
        score += 1 if discipline != "no discipline tilt" else 0
        score += 1 if run_environment != "no run environment tilt" else 0

        if score >= 3:
            classification = "signal"
        elif score == 2:
            classification = "lean signal"
        else:
            classification = "variance"

        summary = ", ".join(active) if active else "no clear tilt detected"

        return {
            "contact_quality": contact_quality,
            "discipline": discipline,
            "run_environment": run_environment,
            "classification": classification,
            "summary": summary,
        }
