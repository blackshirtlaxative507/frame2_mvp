import streamlit as st

# page title
st.title("red sox era comparison")

st.markdown("""
### observation
different eras of baseball create different run environments.

### mechanism
rules, roster construction, analytics, and league strategy shift the run-scoring ecosystem.

### implication
comparing eras requires context — not just raw stats.
""")

# example era dataset
ERA_DATA = {
    "1967–1975": {
        "theme": "pitching dominated",
        "avg_runs_per_game": 3.9,
        "mechanism": "large ballparks + pitching dominance"
    },
    "1995–2004": {
        "theme": "offensive explosion",
        "avg_runs_per_game": 5.2,
        "mechanism": "power surge + smaller parks + expansion"
    },
    "2015–present": {
        "theme": "three true outcomes",
        "avg_runs_per_game": 4.5,
        "mechanism": "analytics + launch angle + bullpen specialization"
    }
}

st.subheader("era environments")

for era, data in ERA_DATA.items():
    st.markdown(f"""
**{era}**

theme: {data["theme"]}  
avg runs/game: {data["avg_runs_per_game"]}  
mechanism: {data["mechanism"]}
""")

st.subheader("tilt signals across eras")

signals = [
    "contact quality",
    "plate discipline",
    "pitch velocity",
    "bullpen leverage",
    "run expectancy swings"
]

for signal in signals:
    st.write(f"- {signal}")