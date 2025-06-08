# Assignment 3: Netflix Data Visualization

## Overview
This project involves exploratory data analysis and visualization of the Netflix Titles dataset. The objective is to extract meaningful insights regarding content type distribution, country-wise content production, genre popularity, and content release trends over the years.

## Dataset
- Source: [Netflix Titles Dataset](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Size: 8807 records, 12 columns
- Key Columns: `type`, `country`, `release_year`, `listed_in` (genres), `date_added`

## Visualizations
The following visualizations were created to analyze the dataset:

1. **Content Type Distribution**  
   Shows the ratio of Movies to TV Shows on Netflix.

2. **Top Countries by Number of Titles**  
   Bar chart displaying the top 10 countries contributing Netflix content.

3. **Content Added Per Year by Type**  
   Year-wise count of movies and TV shows added to Netflix.

4. **Top 10 Genres**  
   Popular genres represented by the number of titles in each.

## How to Run
1. Ensure you have Python 3.x installed along with these libraries:  
   `pandas`, `matplotlib`, `seaborn`

2. Place the `netflix_titles.csv` dataset in the same folder as `netflix_visualization.py`.

3. Run the script:  
   ```bash
   python3 netflix_visualization.py
