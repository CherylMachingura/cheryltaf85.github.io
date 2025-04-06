# Real Estate Market Analysis

## Objective
Analyze and visualize how housing prices interact with interest rates and unemployment rates across U.S. regions to uncover macroeconomic trends.

## Datasets
- Housing Prices: CSV from Kaggle
- Interest Rates: Pulled using the FRED API (Federal Reserve)
- Unemployment Rates: Scraped from a live HTML table on Wikipedia

## Data Preparation
- Cleaned and standardized each data source
- Converted time series data to a consistent monthly format
- Merged datasets using region and month/year keys
- Removed duplicates, handled missing data, and identified outliers via the IQR method

## Tools & Libraries
Python, pandas, matplotlib, seaborn, requests, BeautifulSoup, SQLite

## Visualizations
- Line charts to show housing trends vs. interest rate changes
- Bar charts to compare unemployment and home prices by state
- Correlation heatmaps to explore feature relationships

## Key Findings
- Inverse correlation found between interest rates and housing prices
- Economic downturns reflected clearly in both home values and employment levels
- Multi-source integration provided a more complete economic picture

## Ethical Considerations
- Clearly cited data sources and documented assumptions
- Addressed risks of misinterpreting correlations as causation
- Highlighted the importance of regional and socioeconomic context
