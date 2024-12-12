# Data Sources

This project uses data from the following sources:

1. The Odds API (https://api.the-odds-api.com/)

   - Game odds and totals
   - Historical scores

2. TeamRankings.com
   - Offensive Rankings (https://www.teamrankings.com/nfl/stat/points-per-game)
   - Defensive Rankings (https://www.teamrankings.com/nfl/stat/opponent-points-per-game)

## Data Files

- raw_odds_api.csv: Raw betting odds and game data
- raw_scores_api.csv: Raw scores for historical games
- raw_team_stats.csv: Raw team statistical rankings
- processed_nfl_data.csv: Cleaned and merged dataset that is appended to the overall dataset: nfl_totals_latest
  - This file will NOT be appended for the sake of consistency in our final report
- nfl_totals_latest: Final and overall dataset that includes all data collected from prior weeks and used in analysis
