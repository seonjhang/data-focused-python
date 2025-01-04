import sys
import os
import pandas as pd
import numpy as np
from Crime_cost_scraper import CrimeCostScraper

sys.path.append(os.path.join(os.path.dirname(__file__), '../Scraper'))

class CrimeCostInvoker:
    def __init__(self) -> None:
        pass

    def crimeCostInvoker(self):
        try:
            # Initialize the scraper
            cr = CrimeCostScraper()
            response = cr.crimeCostScraper()

            # Try to find the <div> containing the information
            results_div = response.find('div', id="mg-odata-google-sheet-213")

            # If the div is not found, raise an exception to fall back to CSV
            if not results_div:
                raise ValueError("Couldn't find the results div")

            # Find the table with the specified class
            crime_cost_table = results_div.find_next('table', class_='w-full lining-nums tabular-nums style_table__H8eRl')

            # If the table is not found, raise an exception
            if not crime_cost_table:
                raise ValueError("Couldn't find the crime cost table")

            # Extract the headers from <thead>
            headers = []
            thead = crime_cost_table.find('thead')
            for th in thead.find_all('th'):
                headers.append(th.text.strip())

            # Extract the data rows from <tbody>
            rows = []
            tbody = crime_cost_table.find('tbody')
            for tr in tbody.find_all('tr'):
                row = [td.text.strip() for td in tr.find_all('td')]
                rows.append(row)

            # Create a DataFrame from the extracted data
            df_crime_cost = pd.DataFrame(rows, columns=headers)

            # Save the DataFrame to a CSV file
            df_crime_cost.to_csv('Crime_Rate.csv', index=False)

        except Exception as e:
            print(f"Error during scraping: {e}. Falling back to local CSV.")
            # If scraping fails, load data from the local CSV file
            file_path = os.path.join(os.path.dirname(__file__), '../Data_Files/Crime_Rate.csv')
            if not os.path.exists(file_path):
                print(f"File {file_path} not found! Please ensure it exists.")
                return  # Exit or handle the error as needed
            df_crime_cost = pd.read_csv(file_path, skiprows=1)

        # Process the DataFrame
        df_crime_copy = df_crime_cost.loc[:, ["City", "Crime Cost per Capita"]].copy()

        # Convert "Crime Cost per Capita" to numeric values (remove any dollar signs and commas)
        df_crime_copy["Crime Cost per Capita"] = df_crime_copy["Crime Cost per Capita"].replace(r'[\$,]', '', regex=True).astype(float)

        # Step 4: Define conditions for scoring based on "Crime Cost per Capita"
        conditions = [
            (df_crime_copy["Crime Cost per Capita"] < 597),
            (df_crime_copy["Crime Cost per Capita"] < 775),
            (df_crime_copy["Crime Cost per Capita"] < 1099),
            (df_crime_copy["Crime Cost per Capita"] < 1409),
            (df_crime_copy["Crime Cost per Capita"] < 1807),
            (df_crime_copy["Crime Cost per Capita"] < 2179),
            (df_crime_copy["Crime Cost per Capita"] < 2590),
            (df_crime_copy["Crime Cost per Capita"] < 3267),
            (df_crime_copy["Crime Cost per Capita"] < 4416),
            (df_crime_copy["Crime Cost per Capita"] < 11392)
        ]
        scores = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

        # Use np.select() to assign scores based on conditions, default to 0 if no conditions match
        df_crime_copy["score"] = np.select(conditions, scores, default=0)

        # Sort the DataFrame by "score" in descending order
        df_crime_copy = df_crime_copy.sort_values(by="score", ascending=False)

        # Data cleaning
        df_crime_copy['State'] = df_crime_copy['City'].str.split(',').str[1]
        df_crime_copy['City'] = df_crime_copy['City'].str.split(',').str[0]

        # Specify the output directory
        output_dir = os.path.join(os.path.dirname(__file__), '../Data_Files')
        os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

        # Define the file path for the CSV
        file_path = os.path.join(output_dir, 'Crime_Rate.csv')
        df_crime_copy.to_csv(file_path, index=False)  # Write to CSV
