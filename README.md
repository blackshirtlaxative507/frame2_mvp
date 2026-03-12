# frame² – sports intelligence engine

frame² is a lightweight sports analytics and content engine built to explain games through **process vs result**.

the goal is simple:

**observe → detect the edge → explain the mechanism → generate insights**

---

## core ideas

most fans watch the scoreboard.

frame² tries to explain **why the scoreboard moved**.

the engine focuses on identifying hidden drivers such as:

- contact quality
- plate discipline
- run expectancy swings
- roster structure
- development pipeline

these signals help reveal the **mechanism behind outcomes**.

---

## features

### red sox intelligence dashboard

explore historical eras and identify what drove each team’s success.

### franchise timeline

visualize the full history of the franchise, including:

- world series seasons
- playoff runs
- rebuilding periods
- emerging cores

### core + pipeline explorer

see which players carried each era and how strong the organizational pipeline was.

### history post generator

automatically convert analytics into ready-to-post insights.

---

## screenshots

### core + pipeline explorer
![core explorer](images/frame2_explorer.png)

### franchise timeline
![franchise timeline](images/frame2_franchise_timeline.png)

### history post generator
![history post](images/frame2_post_generator.png)

---

## run locally

```bash
git clone https://github.com/dualityframework-ux/frame2_mvp.git
cd frame2_mvp

pip install -r requirements.txt
streamlit run app.py
