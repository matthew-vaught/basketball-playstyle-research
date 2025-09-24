# Evolution of Power Forward Role in the NBA 🏀

[![Poster Preview](https://raw.githubusercontent.com/matthew-vaught/bball_research_portfolio/main/UGS%20Poster%20Presentation%20Template.pptx%20(4).png)](https://raw.githubusercontent.com/matthew-vaught/bball_research_portfolio/main/UGS%20Poster%20Presentation%20Template.pptx%20(4).png)

This repository contains all notebooks and supporting files for my research on the evolution of height and playstyle for **power forwards** in the NBA from 2013–2014 through 2023–2024.

---

## Background & Motivation

The modern NBA has seen lineup shifts (small ball, positionless basketball) and evolving player archetypes. In particular:

- How has the **average height** of power forwards changed over the past decade?  
- How have playstyles (shot selection, spacing, roles) evolved?  
- Can we classify PFs into distinct archetypes over time and detect transitions?

This project aims to quantify those shifts, cluster PF playstyles, and test whether lineup decisions (e.g. via “small-ball” configurations) statistically correlate with performance gains.

---

## Data & Sources

- **NBA Player & Season Data** scraped from Basketball-Reference and various online sources (Selenium + BeautifulSoup).  
- Data spans 2013–14 through 2023–24, focused on position “PF” players (with allowances for hybrid roles).  
- Key features include per-season stats (points, rebounds, assists, shooting splits, usage), derived metrics (e.g. shot location shares, spacing), etc.  
- Some reference data and external league metrics (for normalization) also imported.

---

## Methods & Tools

- **Tools & Libraries**: Python ecosystem — Pandas, NumPy, scikit-learn, SciPy, Seaborn/Matplotlib.  
- **Dimensionality Reduction / Clustering**:  
  - PCA (Principal Components Analysis)  
  - Ward’s hierarchical clustering  
  - Laplacian Eigenmaps (manifold embedding)  
  - Gap statistic / elbow methods for choosing cluster count  
- **Statistical Testing & Comparative Analyses**: regression slopes, p-values, performance differentials, lineup vs non-lineup comparisons.

---

## Key Findings & Insights

- The **average height** of PFs has trended downward (or plateaued) relative to historical expectations.  
- Distinct **archetypes** emerged (e.g. “stretch PF,” “rim-oriented PF,” “hybrid big”) based on shot location, usage, and role metrics.  
- Over time, many PFs shifted toward spacing and 3-point shooting.  
- Evidence suggests lineup adjustments (e.g. inserting a smaller, more versatile PF) corresponded with **~10% improvement** in win rate on average.  
- Visualizations (scatter plots, clustering maps, temporal embeddings) illustrate these transitions and groupings.

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
2. Move to **Reproducing Results Notebooks/** for the main analysis pipeline: PCA, clustering, and statistical testing.  
3. Explore **tSNE and LE Notebooks/** for embedding plots and visual transitions.  
4. Use files in **Important DataFrames/** to inspect intermediate artifacts.  
5. For additional or exploratory directions, see **Further Research/**.  

*(The code is intended for exploration in a standard Python data science environment; detailed environment setup is not included.)*

---

## Limitations & Future Work

- Classification of PFs may miss hybrid or reclassified players.  
- Some seasons/players have missing data or outlier stats.  
- Future improvements could include:  
  - Extending scraping to more seasons  
  - Integrating tracking data (player movement, shot charts)  
  - Testing predictive models (e.g. archetype → team success)  
  - Developing richer dashboards for interactive exploration  

---

## Acknowledgments

Thanks to my mentor, **Justin Eldridge**, for feedback and guidance throughout this project.  
Additional thanks to Basketball-Reference and NBA APIs for open data access.  
