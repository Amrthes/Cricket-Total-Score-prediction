# ODI Batsmen Data Analysis

## Overview

Analyze career batting statistics of top ODI players using **Python**, **Pandas**, **Matplotlib**, and **Seaborn**. Includes data cleaning, feature engineering, statistical analysis, and visualizations.

---

## Dataset

* **File:** `odb.csv`
* **Records:** 119 players
* **Columns:** Player, Span, Matches (Mat), Innings (Inns), Not Outs (NO), Runs, High Score (HS), Average (Ave), Balls Faced (BF), Strike Rate (SR), 100s, 50s, Ducks (0s), 4s, 6s

---

## Data Cleaning & Feature Engineering

* Removed unnecessary column `Unnamed: 0`.
* Converted `HS` to numeric (`hs_runs`) and added `hs_not_out` flag.
* Cleaned `4s` and `6s` columns, adding flags for "+" values.
* Final features include numeric stats and derived flags for analysis.

---

## Analysis & Visualizations

* **Distributions:** Mat, Inns, BF, SR, Runs (histograms with KDE).
* **Scatter Plot:** Total Runs vs Matches Played.
* **Correlation Matrix:** Visualize relationships between numeric stats.
* **Pie Charts:**

  * Centuries, Half-Centuries, Ducks, Fours, Sixes distribution.
  * Out vs Not Out distribution.
* **Skewness:** Checked for numeric columns, showing slight positive skew.

---

## Key Insights

* Players with Not Out in their High Score: 47
* Players with 4s+: 17 | Players with 6s+: 16
* Total centuries, half-centuries, and boundaries analyzed across all players.
* Most players have slightly skewed distributions for runs, matches, and strike rate.

---

## How to Run

1. Install packages:

```bash
pip install pandas matplotlib seaborn
```

2. Place `odb.csv` in your working directory.
3. Run the Python script or Jupyter notebook to explore data and visualizations.

---

