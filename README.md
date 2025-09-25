# Evolution of Playstyle and Height in the NBA 🏀

[![Poster Preview](https://raw.githubusercontent.com/matthew-vaught/bball_research_portfolio/main/UGS%20Poster%20Presentation%20Template.pptx%20(4).png)](https://raw.githubusercontent.com/matthew-vaught/bball_research_portfolio/main/UGS%20Poster%20Presentation%20Template.pptx%20(4).png)

This repository contains all notebooks and supporting files for my research on the evolution of height and playstyle in the NBA from 2000 through 2024.

---

## Background & Motivation

The modern NBA has seen lineup shifts (small ball, positionless basketball) and evolving player archetypes. In particular:

- How has the **average height** of players changed over the past few decades?  
- How have playstyles (shot selection, spacing, roles) evolved?  
- Can we classify lineups into archetypes and detect transitions over time?

This project aims to quantify those shifts, analyze playstyle archetypes, and test whether lineup decisions (e.g. via “small-ball” configurations) statistically correlate with performance gains.

---

## Data & Sources

- **NBA Player & Season Data** scraped from Basketball-Reference and various online sources (Selenium + BeautifulSoup).  
- Data spans the 2000–01 through 2023–24 seasons, focusing on both playstyle and height statistics.  
- Key features include per-season stats (points, rebounds, assists, shooting splits, usage), derived metrics (e.g. shot location shares, spacing), as well as height and athleticism statistics from then NBA combine.

---

## Methods & Tools

- **Tools & Libraries**: Python — Pandas, NumPy, scikit-learn, SciPy, Seaborn/Matplotlib.  
- **Dimensionality Reduction / Clustering**:  
  - PCA (Principal Components Analysis)  
  - Ward’s hierarchical clustering  
  - Laplacian Eigenmaps (manifold embedding)  
  - Gap statistic / elbow methods for choosing cluster count  
- **Statistical Testing & Comparative Analyses**: regression slopes, p-values, performance differentials, lineup vs non-lineup comparisons.

---

## Key Findings & Insights

- The NBA has shifted to a "small-ball" era, with shorter teams on average and a quicker style of play with more 3 pointers being taken
- Specifically, teams have gone towards shorter overall lineups with traditional "big men" being replaced by slightly shorter, more athletic power forwards and centers
- During the early periods of this transition, teams who embodied the new playstyle and height trends the most (the most "trendy" teams) boasted a win percentage over **10% higher** than those teams who failed to adjust to the trend as quickly
- Visualizations (scatter plots, clustering maps, temporal embeddings) illustrate these transitions more eloquently.

---

## Interactive Dashboards

Explore interactive visualizations that highlight the results of this research:

- [Team Trends Over Years](https://matthew-vaught.github.io/team_trend_over_years_visualization/) — interactive view of team trends over time.  
- [Laplacian Eigenmaps with Histograms](https://matthew-vaught.github.io/le_with_histograms/) — embedding visualization with detailed histograms.  
- [LE Slider with Win Percentage](https://matthew-vaught.github.io/new_le_slider_winp/) — slider tool to explore embeddings alongside win percentage.  

---

## Repository Structure

```
basketball-pf-research/
│
├── Basketball-reference data/ # raw and processed stats from Basketball-Reference
├── nba.com data/ # supplementary data from NBA site APIs
├── Data to Replicate Richardson’s Results/
├── Further Research/ # exploratory notebooks and extensions
├── Important DataFrames/ # saved data artifacts (CSV/pickle)
├── Importing Data Notebooks/ # scraping and data cleaning notebooks
├── Reproducing Results Notebooks/ # main analysis pipeline notebooks
├── tSNE and LE Notebooks/ # dimensionality reduction / embedding analyses
└── README.md
```

---

## How to Explore / Use This Repo

1. Start with **Importing Data Notebooks/** to see how raw data is collected and cleaned.  
2. Move to **Reproducing Results Notebooks/** for the preliminary analysis: reproducing the results from a paper I found that used PCA and clustering to create archetypes for player playstyles.  
3. Explore **tSNE and LE Notebooks/** for the main analysis, where I primarily used Laplacian Eigenmaps and PCA to visualize high-dimensional height and playstyle metrics and determine long-term trends.  
4. Use files in **Important DataFrames/** to inspect intermediate artifacts.  
5. For additional research on how athleticicism covaried with the shift in height, see **Further Research/**.  

---

## Limitations & Future Work

- Classification of PFs may miss hybrid or reclassified players.  
- Some seasons/players have missing data or outlier stats.  
- Future improvements could include:  
  - Extending scraping to more seasons 
  - Integrating tracking data (player movement, shot charts)  
  - Testing predictive models (e.g. archetype → team success)

---

## Acknowledgments

Thanks to my mentor, **Justin Eldridge**, for feedback and guidance throughout this project.  
Additional thanks to Basketball-Reference and NBA APIs for open data access.  
