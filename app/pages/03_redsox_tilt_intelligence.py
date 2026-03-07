import streamlit as st

st.set_page_config(page_title="red sox tilt intelligence")

st.title("red sox tilt intelligence")

st.markdown(
"""
### observation
games shift when one hidden mechanism tilts the environment.

### mechanism
contact quality  
plate discipline  
run expectancy swings

### implication
if one of these tilts consistently, the scoreboard usually follows.
"""
)

st.subheader("tilt signals")

signals = [
    "barrel rate",
    "chase rate",
    "whiff rate",
    "run expectancy change",
]

for signal in signals:
    st.write("- " + signal)