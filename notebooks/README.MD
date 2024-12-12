# Analysis Notebooks

The analysis is split into three notebooks that should be run in the following order:

1. `00_data_collection.ipynb`

   - Collects raw data from The Odds API and TeamRankings.com
   - Saves raw data files with minimal processing
   - Creates raw_odds_api.csv , raw_scores_api.csv, and raw_team_stats.csv

2. `01_data_processing.ipynb`

   - Merges and cleans the raw data files
   - Creates processed_nfl_data.csv

3. `02_analysis.ipynb`
   - Performs descriptive analysis
   - Generates visualizations and insights
