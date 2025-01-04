# data-focused-python
CMU courses, 95-888 Data Focused Python
[Course site](https://api.heinz.cmu.edu/courses_api/course_detail/95-888/)


## Proejct Description
**Project Name: BestNest**

BestNest is a data-driven application that helps users find the ideal city to live in based on their preferences. It analyzes various factors such as cost of living, literacy rate, crime cost, and air quality to recommend the best city for each user.

**Features:**
Interactive user interface built with Streamlit
Data analysis and visualization using pandas, numpy, matplotlib, and seaborn
Web scraping capabilities for real-time data collection
Customizable city recommendations based on user-selected parameters
Visualization of results through tables and heatmaps
Code Modularisation for easy understanding and execution.

**Installation:**
You will require a python IDE.

Install the required dependencies:

pip install -r requirements.txt

**Usage:**
Run the Streamlit application:
streamlit run BestNest.py. Run it from the terminal.

Or directly go to below link.
https://bestnest.streamlit.app/

You can select any number of parameter and basis the selection you will get the list of top 10 cities.

## Data Sources

**1. Cost of Living :** https://advisorsmith.com/data/coli/

Cost of Living Index is modeled upon national average household budgets, with weights assigned to six major categories of household expenses. 
The expense categories along with their weights are listed below:

Food: 16.1%
Housing: 23.2%
Utilities: 10.1%
Transportation: 18.6%
Healthcare: 9.6%
Consumer Discretionary Spending: 22.3%
These categories are aggregated to produce a cost of living index value for each of the cities.

**2. Crime Cost :** https://www.moneygeek.com/living/safest-cities/

MoneyGeek’s annual analysis looks at the most recent crime statistics from the Federal Bureau of Investigation (FBI) to estimate the cost of crime in 302 cities with populations greater than 100,000 across the United States. 
The analysis pairs reported crime statistics with academic research on the societal costs of different types of crimes to estimate the cost of crime for each city.


**3. Literacy Rate :** https://wallethub.com/edu/e/most-and-least-educated-cities/6656

Total Literacy score for a City includes  including “Educational Attainment” and “Quality of Education & Attainment Gap.” From the survey conducted by Wallet Hub team. The higher the Total Score more literate is the city.

**4.Air Quality :** https://aqs.epa.gov/aqsweb/airdata/download_files.html#Annual

AQI is calculated each day for each monitor for the Criteria Gases and PM10 and PM2.5 (FRM and non FRM).

*Note :
Literacy Rate website only allow us once to scrape the website once. 
Hence we download the data in a csv and utilise it here if the status response is 403.*


Normalisation of scoring:

Since the scale of scoring was different for all the parameters we scraped from the internet we normalised the scores out of 10. 10 being the best and 1 being the worst and calculated the total score based on the parameters selected by the user and ranked the cities based on descending order of their scores.

## Structure
<img width="764" alt="image" src="https://github.com/user-attachments/assets/048f300c-4078-42d2-a380-f73954a75abe" />

